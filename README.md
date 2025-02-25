# Script para el envío automático de correos electrónicos

## Configuración

1. Crear un ambiente virtual de Python y activarlo:

```bash
python3 -m venv env
source env/bin/activate
```

2. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

3. Configurar las variables de entorno:
   Cree un archivo `.env` en la raíz del proyecto, basándose en el archivo `sample.env`, y complete los siguientes campos:

- `SENDER_EMAIL`: Correo electrónico desde el cual se enviarán los correos. Debe ser una cuenta de Gmail.
- `SENDER_PASSWORD`: Contraseña de la cuenta de correo, que debe ser una contraseña de aplicación. Puede generar una aquí: https://myaccount.google.com/apppasswords

## Uso

1. Generar la plantilla HTML:
   Cree una plantilla HTML con los placeholders que desee reemplazar. Los placeholders deben tener el formato `{placeholder}`, por ejemplo `{user_name}`. Además, la primera línea de la plantilla debe contener el asunto del correo en un comentario HTML, como en el siguiente ejemplo: `<!-- Asunto: Bienvenido a Nuestro Servicio -->`.

2. Crear el archivo CSV con los destinatarios:
   El archivo CSV debe contener una columna llamada `user_email`, que será utilizada para almacenar las direcciones de los destinatarios. Las columnas adicionales deben coincidir con los placeholders en la plantilla HTML, ya que se utilizarán para reemplazarlos durante el envío.

3. Consultar los archivos de ejemplo adjuntos:
   Puede hacer referencia a los archivos de ejemplo proporcionados para entender el formato y la estructura de los archivos necesarios.

4. Ejecutar el script main.py:
   Ejecute el script main.py pasando como parámetros la ruta del archivo CSV de destinatarios y la ruta de la plantilla HTML:

```bash
python3 main.py <path_to_data> <path_to_template>
```
