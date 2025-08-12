# Guía Avanzada de Solución de Problemas de Impresora

### **Introducción: Entendiendo los Fallos de Impresión**

Los problemas de impresión son una de las interrupciones más comunes y frustrantes en el día a día. Generalmente, el error "Mis documentos no se imprimen" se debe a una de tres posibles causas: un problema de hardware en la propia impresora, un problema de conectividad de red o un problema de software en tu computador.

Este documento te guiará con un enfoque sistemático, desde las verificaciones más simples hasta las soluciones más técnicas, para que puedas resolver la mayoría de los inconvenientes por ti mismo. Las impresoras del banco siguen una convención de nombres lógica para facilitar su identificación, como `PISO7-COLOR-01`, que indica su ubicación física y tipo.

### **Nivel 1: Verificaciones Esenciales y Físicas**

Antes de tocar la configuración de tu equipo, revisa los aspectos más básicos.

1.  **Verificar el Estado de la Impresora:** Asegúrate de que la impresora esté encendida, tal como lo indica su panel de control o un LED de estado. Revisa la pantalla LCD de la impresora en busca de mensajes de error explícitos como "Atasco de Papel", "Tóner Bajo" o "Bandeja Vacía".
2.  **Verificar la Conexión de Red:** Confirma que estás conectado a la red correcta del banco. Debes usar la red Wi-Fi corporativa (ej. "BancoXYZ_Corp") o estar conectado por cable. La red de "Invitados" no tiene acceso a las impresoras. Si trabajas de forma remota, es obligatorio estar conectado a la VPN.
3.  **Seleccionar la Impresora Correcta:** Al momento de imprimir, se abre un cuadro de diálogo. Asegúrate de que en la lista desplegable esté seleccionada la impresora correcta a la que deseas enviar el trabajo (ej. `PISO7-COLOR-01`). Un error común es tener seleccionada una impresora antigua o una impresora virtual como "Microsoft Print to PDF".

### **Nivel 2: Solución de Problemas de Software**

Si todo lo físico parece estar en orden, el problema probablemente reside en tu PC.

1.  **Reiniciar el Servicio de Cola de Impresión (Spooler):** El "Print Spooler" es un servicio de Windows que gestiona la lista de documentos en espera de ser impresos. A veces se bloquea.
    -   Presiona las teclas `Win + R` para abrir el cuadro "Ejecutar".
    -   Escribe `services.msc` y presiona Enter.
    -   En la lista de servicios, busca "Cola de impresión" (o "Print Spooler").
    -   Haz clic derecho sobre él y selecciona "Reiniciar". Esto forzará la limpieza de trabajos atascados.
2.  **Limpieza Manual de la Cola de Impresión:** Si reiniciar el servicio no funciona, puedes vaciar manualmente la carpeta donde se almacenan los trabajos.
    -   Abre `services.msc` de nuevo, haz clic derecho en "Cola de impresión" y selecciona "Detener".
    -   Abre el Explorador de Archivos y navega a `C:\Windows\System32\spool\PRINTERS`.
    -   Elimina todos los archivos dentro de esta carpeta (puede que necesites permisos de administrador).
    -   Vuelve a la ventana de servicios, haz clic derecho en "Cola de impresión" y selecciona "Iniciar".

### **Preguntas Frecuentes y Escalado**

* **P: Mis impresiones salen con rayas o mala calidad.**
    * **R:** Esto es un problema del hardware de la impresora, no de tu PC. Generalmente indica que el cartucho de tóner está bajo. Por favor, reporta el problema al personal administrativo de tu piso para que soliciten un reemplazo o mantenimiento.
* **P: ¿Cómo agrego una impresora de otro piso?**
    * **R:** Ve a "Configuración > Dispositivos > Impresoras y escáneres", haz clic en "Agregar una impresora o escáner" y busca el nombre en el directorio.
* **P: Nada de esto funcionó. ¿Qué información necesita la mesa de ayuda?**
    * **R:** Para agilizar tu solicitud, ten a mano tu nombre de equipo (hostname), el nombre exacto de la impresora, la aplicación desde la que intentas imprimir y cualquier mensaje de error que aparezca.