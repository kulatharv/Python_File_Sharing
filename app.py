#import modules 

#to work with HTTP Web servers
import http.server

#to access BSD socket interface
import socket

#to work with network servers
import socketserver

#to display the documents to user on other device as a web page
import webbrowser

#to generate a qr code
import pyqrcode
from pyqrcode import QRCode

#to convert the code in png format
import png

#to access all directories and os
import os

#assign port
PORT = 8010

#to find the name of user's system
os.environ['USERPROFILE']

#changing the path 
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']))
                      
#handler to serve files from appropriate directory
class DesktopHandler(http.server.SimpleHTTPRequestHandler):
   def translate_path(self, path):
      #to get the absolute path
      root_dir = os.path.abspath(desktop)
      #to join the root directory and the given path
      path = os.path.normpath(path)
      words = path.split('/')
      words = filter(None, words)
      path = root_dir
      for word in words:
         if os.path.dirname(word) or word in (os.curdir, os.pardir):
            continue
         path = os.path.join(path, word)
      return path


#create http request
Handler = DesktopHandler
hostname = socket.gethostname()


#to find the IP address of pc
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = "http://" + s.getsockname()[0] + ":" + str(PORT)
link = IP

#convert the IP address into a Qrcode using pyqrcode
url = pyqrcode.create(link)
url.svg("myqr.svg", scale=8)
webbrowser.open('myqr.svg')

#create http request and serve folders between client and server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
   print("serving at port", PORT)
   print("Type this in your Browser", IP)
   print("or Use the QRCode")
   httpd.serve_forever()