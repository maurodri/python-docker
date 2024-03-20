#!/usr/bin/python3
import subprocess,os
from http.server import BaseHTTPRequestHandler,HTTPServer

PORT_NUMBER = 8082

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):

  #Handler for the GET requests
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type','text/html')
    self.end_headers()
    # Send the html message
    self.wfile.write("*** Python - Hello World ! ***\n".encode())
    self.wfile.write(("WELCOME_MSG : " + os.getenv('WELCOME_MSG', 'undef')).encode() )
    self.wfile.write("\n".encode())
    self.wfile.write(("Hostname is : " + subprocess.check_output("uname -n", shell=True).decode()).encode())
    self.wfile.write(("Process ID  : " + str(os.getpid())).encode())
    return

try:
  #Create a web server and define the handler to manage the
  #incoming request
  server = HTTPServer(('', PORT_NUMBER), myHandler)
  print('Started httpserver on port ', PORT_NUMBER)

  #Wait forever for incoming htto requests
  server.serve_forever()

except KeyboardInterrupt:
  print('^C received, shutting down the web server')
  server.socket.close()
