#!/usr/bin/python3
# Esta línea indica que el script debe ser ejecutado usando Python 3.

import subprocess,os
# Importa los módulos 'subprocess' y 'os'. 'subprocess' permite ejecutar comandos del sistema operativo, y 'os' proporciona funciones para interactuar con el sistema operativo.

from http.server import BaseHTTPRequestHandler,HTTPServer
# Importa las clases 'BaseHTTPRequestHandler' y 'HTTPServer' del módulo 'http.server'. Estas clases se utilizan para crear un servidor HTTP.

PORT_NUMBER = 8082
# Define el número de puerto en el que se ejecutará el servidor.

class myHandler(BaseHTTPRequestHandler):
# Define una clase llamada 'myHandler' que hereda de 'BaseHTTPRequestHandler'. Esta clase manejará las solicitudes HTTP que lleguen al servidor.

  def do_GET(self):
  # Define un método para manejar las solicitudes GET HTTP.
    self.send_response(200)
    # Envía una respuesta HTTP 200, que significa 'OK'.
    self.send_header('Content-type','text/html')
    # Añade una cabecera al HTTP response especificando que el contenido será HTML.
    self.end_headers()
    # Termina las cabeceras HTTP.
    self.wfile.write("*** Python - Hello World ! ***\n".encode())
    # Envía un mensaje al cliente.
    self.wfile.write(("WELCOME_MSG : " + os.getenv('WELCOME_MSG', 'undef')).encode() )
    # Envía un mensaje de bienvenida, que se obtiene de las variables de entorno.
    self.wfile.write("\n".encode())
    self.wfile.write(("Hostname is : " + subprocess.check_output("uname -n", shell=True).decode()).encode())
    # Envía el nombre del host.
    self.wfile.write(("Process ID  : " + str(os.getpid())).encode())
    # Envía el ID del proceso.
    return

try:
# El bloque 'try' permite probar un bloque de código en busca de errores.
  server = HTTPServer(('', PORT_NUMBER), myHandler)
  # Crea un servidor web y define el manejador para gestionar las solicitudes entrantes.
  print('Started httpserver on port ', PORT_NUMBER)
  # Imprime un mensaje indicando que el servidor ha comenzado.
  server.serve_forever()
  # Inicia el servidor para que escuche indefinidamente las solicitudes HTTP entrantes.

except KeyboardInterrupt:
# El bloque 'except' permite manejar el error. En este caso, se maneja la interrupción de teclado (Ctrl+C).
  print('^C received, shutting down the web server')
  # Imprime un mensaje indicando que se ha recibido una interrupción de teclado.
  server.socket.close()
  # Cierra el servidor web.
