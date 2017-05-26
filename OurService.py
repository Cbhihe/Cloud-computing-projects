#!/usr/bin/env python
import SimpleHTTPServer
import SocketServer

class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
   def do_GET(self):
      if self.path == '/':
         self.path = '/OurService.html'
      return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

Handler = MyRequestHandler
server = SocketServer.TCPServer(('0.0.0.0', 8954), Handler)

print 'Started my REST API on port 8954' 
server.serve_forever()