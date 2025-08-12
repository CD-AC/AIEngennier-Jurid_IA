# Guía Completa para Liberar Espacio en el Disco Duro (C:)

### **Introducción: ¿Por Qué es Crítico Gestionar el Espacio en Disco?**

El mensaje de error "Poco espacio en disco" en la unidad `(C:)` es una alerta crítica que no debe ser ignorada. Un disco duro lleno no solo te impide guardar nuevos documentos, sino que también degrada severamente el rendimiento general de tu equipo, causando lentitud, bloqueos de aplicaciones y, lo más importante, impidiendo la instalación de actualizaciones críticas de seguridad de Windows.

En el Banco XYZ, los equipos portátiles se entregan con una configuración estándar, y la gestión proactiva de tu espacio de almacenamiento es una responsabilidad compartida para asegurar la operatividad y seguridad de tu herramienta de trabajo. Esta guía te ofrece un método seguro y por pasos para recuperar espacio valioso.

### **Paso 1: Usar el Liberador de Espacio en Disco de Windows**
Esta es la herramienta más segura y efectiva para una limpieza inicial.

1.  Abre el menú Inicio, escribe **"Liberador de espacio en disco"** y selecciona la aplicación.
2.  Asegúrate de que esté seleccionada la unidad `(C:)` y haz clic en Aceptar.
3.  La herramienta analizará tu disco. En la ventana de resultados, marca las casillas. Las más importantes suelen ser **"Archivos temporales de Internet"**, **"Papelera de reciclaje"** y **"Archivos temporales"**.
4.  **Paso crucial:** Haz clic en el botón **"Limpiar archivos del sistema"**. Esto reiniciará el análisis con permisos elevados y encontrará archivos mucho más grandes, como restos de instalaciones de Windows Update. Repite el paso 3 y haz clic en Aceptar para iniciar la limpieza.

### **Paso 2: Revisar y Organizar tus Carpetas Personales**
A menudo, el mayor consumo de espacio proviene de archivos acumulados.

1.  **Revisa tu carpeta de "Descargas"**: Es el lugar más común donde se acumulan instaladores, PDFs y archivos ZIP que ya no son necesarios. Bórralos sin miedo.
2.  **Explora tu Escritorio y Documentos**: Revisa estas carpetas en busca de archivos muy pesados (videos, presentaciones grandes, etc.).
3.  **Política del Banco**: Los archivos de trabajo importantes y de gran tamaño deben ser almacenados en la ubicación de red designada (ej. OneDrive for Business o unidades de red compartidas), no permanentemente en tu disco local. Esto no solo libera espacio, sino que también garantiza que tus datos estén respaldados por el banco.

### **Paso 3: Desinstalar Programas No Utilizados**
Las aplicaciones pueden ocupar una cantidad significativa de espacio.

1.  Ve a `Configuración > Aplicaciones > Aplicaciones y características`.
2.  Ordena la lista por **"Tamaño"** para ver rápidamente qué programas consumen más espacio.
3.  Desinstala cualquier software que ya no utilices, **siempre y cuando no sea software corporativo**.
4.  **Advertencia:** **NO DESINSTALES** software esencial del banco como la suite de Microsoft Office, clientes de VPN (GlobalProtect), agentes de seguridad (antivirus) o cualquier herramienta con el nombre del banco. Su eliminación puede dejar tu equipo fuera de cumplimiento y sin funcionar correctamente.

### **Advertencia Final y Cuándo Pedir Ayuda**

Bajo ninguna circunstancia debes borrar o modificar archivos manualmente dentro de las siguientes carpetas:
-   `C:\Windows`
-   `C:\Program Files`
-   `C:\Program Files (x86)`
-   `C:\ProgramData`
-   `C:\Users\tu_usuario\AppData`

Eliminar archivos de estas ubicaciones puede dañar permanentemente tu sistema operativo, requiriendo una reinstalación completa por parte del equipo de TI.

Si has seguido todos estos pasos y continúas con problemas de espacio, por favor, crea un ticket con la mesa de ayuda para un análisis más profundo.