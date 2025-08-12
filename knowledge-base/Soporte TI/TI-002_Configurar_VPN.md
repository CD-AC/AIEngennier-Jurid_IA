# Guía Exhaustiva de Configuración y Uso de la VPN Corporativa (GlobalProtect)

### **Introducción: ¿Qué es la VPN y Por Qué es Esencial en el Banco?**

Una Red Privada Virtual (VPN, por sus siglas en inglés) es una tecnología de seguridad que crea un "túnel" encriptado y seguro a través de una red pública como internet. En el Banco XYZ, la VPN GlobalProtect es una herramienta fundamental que te permite conectar tu equipo a la red interna del banco desde cualquier lugar del mundo, como si estuvieras físicamente en tu escritorio en la oficina.

El uso de la VPN es **obligatorio** para acceder a la mayoría de los recursos corporativos de forma remota, incluyendo unidades de red compartidas, aplicaciones internas, portales de desarrollo y servicios como la impresión en red. Esta medida garantiza que toda la información que viaja entre tu computador y los servidores del banco esté protegida contra interceptaciones y accesos no autorizados, cumpliendo con las más altas normativas de seguridad bancaria. Ya conectado, puedes acceder a los recursos internos del banco.

Este documento detalla el proceso de instalación, conexión y solución de problemas de la VPN GlobalProtect.

### **1. Proceso de Instalación desde el Portal de Software**
La instalación del cliente VPN está centralizada para garantizar que siempre tengas la versión correcta y aprobada por el banco.

1.  Localiza y abre el **"Portal de Software"** que se encuentra en el escritorio de tu computador corporativo. Si no lo encuentras, búscalo en el menú Inicio de Windows.
2.  Dentro del portal, utiliza la barra de búsqueda para encontrar la aplicación **"GlobalProtect VPN"** y haz clic en **"Instalar"**.
3.  El proceso es totalmente automatizado y gestionado por el sistema; no se requiere ninguna intervención por tu parte y ya cuenta con los permisos de administrador necesarios.
4.  Una vez finalizada la instalación, aparecerá un nuevo icono con forma de globo terráqueo en tu barra de tareas, usualmente cerca del reloj del sistema.

### **2. Realizando tu Primera Conexión**
Con el cliente ya instalado, el siguiente paso es configurarlo para que apunte a la infraestructura del banco.

1.  Haz clic en el **icono del globo terráqueo gris** en tu barra de tareas. Se abrirá una pequeña ventana.
2.  En el campo de "Portal", ingresa la siguiente dirección: `vpn.bancoxyz.com`.
3.  Haz clic en el botón **"Conectar"**.

### **3. Autenticación de Múltiples Factores (MFA)**
Para máxima seguridad, la conexión requiere dos pasos de verificación.

1.  El sistema te solicitará tu **usuario y contraseña de Windows**. Son los mismos que usas para iniciar sesión en tu computador.
2.  A continuación, recibirás una notificación push en la aplicación **"Microsoft Authenticator"** en tu teléfono móvil registrado. Deberás **aprobar** la solicitud de inicio de sesión en tu celular.

### **4. Verificación y Uso**
- ¡Listo! El icono del globo terráqueo cambiará a un **color azul con un escudo**, confirmando que estás conectado de forma segura.
- Para desconectarte, simplemente haz clic en el icono azul y selecciona "Desconectar".

### **Solución de Problemas y Preguntas Frecuentes**

* **P: No recibo la notificación en Microsoft Authenticator. ¿Qué hago?**
    * **R:** Asegúrate de que tu celular tenga conexión a internet. Abre la app de Authenticator manualmente; a veces la solicitud está esperando adentro. Si todo falla, contacta a la mesa de ayuda, es posible que tu cuenta necesite resincronizarse.
* **P: El icono se queda en gris o dice "Conectando..." pero nunca termina.**
    * **R:** Verifica tu conexión a internet local. Intenta reiniciar tu router. Si el problema persiste, reinicia tu equipo para refrescar todos los servicios de red.
* **P: Estoy conectado a la VPN pero sigo sin poder acceder a una unidad de red.**
    * **R:** La VPN te da acceso a la red, pero aún necesitas los permisos correctos para cada recurso. Si puedes acceder a unas cosas y a otras no, el problema puede ser de permisos. Contacta a la mesa de ayuda e indica a qué recurso específico no puedes acceder.
* **P: ¿La VPN hace que mi internet sea más lento?**
    * **R:** Es normal una ligera reducción de velocidad debido a la encriptación. Si la lentitud es extrema, puede deberse a la calidad de tu red de internet local.