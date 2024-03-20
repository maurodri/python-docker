FROM python:3.12-rc-slim

# Copy the Python script to the Docker image
COPY hello-world.py /usr/src/app/hello-world.py

EXPOSE 8082

ENTRYPOINT ["python", "/usr/src/app/hello-world.py"]

LABEL org.opencontainers.image.source https://github.com/robertshand/python-helll-world
