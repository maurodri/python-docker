# Este Dockerfile comienza con la imagen base de Python versión 3.12 Release Candidate (rc) en su versión slim (una versión minimalista de la imagen de Python)
FROM python:3.12-rc-slim

# Copia el script de Python 'hello-world.py' desde tu máquina local al directorio '/usr/src/app/' en la imagen de Docker
COPY hello-world.py /usr/src/app/hello-world.py

# Expone el puerto 8082 para permitir la comunicación con la aplicación en la imagen de Docker
EXPOSE 8082

# Define el comando que se ejecutará cuando se inicie un contenedor a partir de esta imagen de Docker. En este caso, se ejecutará el script de Python 'hello-world.py'
ENTRYPOINT ["python", "/usr/src/app/hello-world.py"]

# Añade una etiqueta a la imagen de Docker con la URL del repositorio de código fuente
LABEL org.opencontainers.image.source https://github.com/robertshand/python-helll-world
