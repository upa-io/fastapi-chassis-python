# Usamos la imagen base de Python 3.9.17 con una versión "slim" para un contenedor más ligero
FROM python:3.12.6-slim

# Crear un usuario no privilegiado llamado "appuser"
RUN adduser --disabled-password --gecos "" appuser

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /code

# Copiamos el archivo requirements.txt del directorio local al directorio /code del contenedor
COPY ./requirements.txt /code/requirements.txt

# Instalamos las dependencias listadas en requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copiamos el contenido del directorio ./app del directorio local al directorio /code/app del contenedor
COPY ./app /code/app

# Cambiamos el usuario predeterminado para ejecutar la aplicación en el contenedor
USER appuser

# Comando que se ejecutará al iniciar el contenedor: inicia la aplicación FastAPI con Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]