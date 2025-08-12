from __future__ import annotations

import pendulum
from airflow.models.dag import DAG
from airflow.decorators import task

# Importar hooks para conectarse a los servicios
from airflow.providers.microsoft.azure.hooks.wasb import WasbHook
from airflow.providers.mongo.hooks.mongo import MongoHook
from airflow.providers.pinecone.hooks.pinecone import PineconeHook
from airflow.providers.openai.hooks.openai import OpenAIHook

# Importar las librerías de LangChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
import pinecone


# CONFIGURACIÓN CENTRALIZADA

PINECONE_INDEX_NAME = "jurid-ia-idx"
EMBEDDING_MODEL_NAME = "text-embedding-3-small"
EMBEDDING_DIMENSION = 1536
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150


# DEFINICIÓN DEL DAG

with DAG(
    dag_id="jurid_ia_knowledge_base_etl",
    start_date=pendulum.datetime(2025, 8, 11, tz="UTC"),
    schedule="@daily",  # Ejecutar todos los días a medianoche
    catchup=False,
    doc_md="""
    ETL para construir y actualizar la base de conocimiento de Jurid-IA.
    Extrae datos de Azure Blob y MongoDB, los vectoriza y los carga en Pinecone.
    """,
    tags=["jurid-ia", "rag", "etl"],
) as dag:

    @task
    def clear_pinecone_index() -> None:
        """Tarea para eliminar el índice de Pinecone y empezar de cero."""
        print(f"Borrando el índice '{PINECONE_INDEX_NAME}' si existe...")
        pinecone_hook = PineconeHook(conn_id="pinecone_conn")
        conn = pinecone_hook.get_conn()
        if PINECONE_INDEX_NAME in conn.list_indexes().names():
            conn.delete_index(PINECONE_INDEX_NAME)
            print("Índice borrado.")
        
        print(f"Creando un nuevo índice '{PINECONE_INDEX_NAME}'...")
        conn.create_index(
            name=PINECONE_INDEX_NAME,
            dimension=EMBEDDING_DIMENSION,
            metric='cosine'
        )
        print("Nuevo índice creado.")


    @task
    def extract_from_blob_storage() -> list[dict]:
        """Extrae archivos de texto desde Azure Blob Storage."""
        print("Extrayendo archivos de Azure Blob Storage...")
        wasb_hook = WasbHook(wasb_conn_id="azure_blob_conn")
        container_name = "knowledge-base"
        documents = []

        # Tu lógica para listar y descargar archivos
        for blob_name in wasb_hook.get_blobs_list(container_name=container_name):
            content = wasb_hook.read_file(container_name=container_name, blob_name=blob_name)
            documents.append({"page_content": content, "metadata": {"source": blob_name}})
        
        print(f"Se extrajeron {len(documents)} documentos de Blob Storage.")
        return documents

    @task
    def extract_from_mongodb() -> list[dict]:
        """Extrae documentos desde MongoDB."""
        print("Extrayendo documentos de MongoDB...")
        mongo_hook = MongoHook(mongo_conn_id="mongo_conn")
        docs = mongo_hook.find(mongo_collection="contratos", query={}, mongo_db="juridico")
        
        documents = []
        for doc in docs:
            content = f"Cliente: {doc.get('cliente', '')}. Objeto del contrato: {doc.get('objeto', '')}. Términos: {doc.get('terminos', '')}"
            documents.append({"page_content": content, "metadata": {"source": f"MongoDB/contratos/{doc['_id']}"}})

        print(f"Se extrajeron {len(documents)} documentos de MongoDB.")
        return documents

    @task
    def process_and_vectorize(blob_docs: list[dict], mongo_docs: list[dict]) -> list[dict]:
        """Combina, divide y vectoriza todos los documentos."""
        print("Procesando y vectorizando documentos...")
        all_docs_content = blob_docs + mongo_docs
        
        if not all_docs_content:
            raise ValueError("No se encontraron documentos para procesar.")

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)

        docs_to_split = [doc['page_content'] for doc in all_docs_content]
        chunks_text = text_splitter.split_text(docs_to_split)
        
        print(f"Total de fragmentos (chunks) creados: {len(chunks_text)}")

        # Ahora generamos los embeddings
        openai_hook = OpenAIHook(conn_id='openai_conn')
        embeddings_model = OpenAIEmbeddings(openai_api_key=openai_hook.api_key, model=EMBEDDING_MODEL_NAME)
        
        vectors = embeddings_model.embed_documents(chunks_text)
        
        # Combinamos los chunks con sus vectores y metadatos
        vectorized_chunks = []
        for i, chunk in enumerate(chunks_text):
            vectorized_chunks.append({
                "id": f"chunk_{i}",
                "values": vectors[i],
                "metadata": {"text": chunk}
            })
            
        return vectorized_chunks

    @task
    def load_to_pinecone(vectorized_chunks: list[dict]) -> None:
        """Carga los chunks vectorizados en Pinecone."""
        if not vectorized_chunks:
            print("No hay chunks para cargar. Saltando la tarea.")
            return

        print(f"Cargando {len(vectorized_chunks)} chunks en Pinecone...")
        pinecone_hook = PineconeHook(conn_id="pinecone_conn")
        pinecone_index = pinecone_hook.get_conn().Index(PINECONE_INDEX_NAME)
        
        # Cargar en lotes para mayor eficiencia
        for i in range(0, len(vectorized_chunks), 100):
            batch = vectorized_chunks[i:i + 100]
            pinecone_index.upsert(vectors=batch)
        
        print("Carga en Pinecone completada.")

 
    # DEFINICIÓN DE DEPENDENCIAS DEL DAG

    clear_index_task = clear_pinecone_index()
    blob_docs_task = extract_from_blob_storage()
    mongo_docs_task = extract_from_mongodb()
    
    vectorize_task = process_and_vectorize(
        blob_docs=blob_docs_task,
        mongo_docs=mongo_docs_task
    )
    
    load_task = load_to_pinecone(vectorized_chunks=vectorize_task)

    clear_index_task >> [blob_docs_task, mongo_docs_task] >> vectorize_task >> load_task