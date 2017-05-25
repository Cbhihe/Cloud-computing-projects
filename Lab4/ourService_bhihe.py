""" Simple HTTP request handler based on Python SimpleHTTPServer """

#!/usr/bin/env python
import SimpleHTTPServer  # module merged in http.server in Py3.
import SocketServer

class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
""" ---- """
    # serves files from the current directory and below,
    # directly mapping the directory structure to HTTP requests.

    def do_GET(self):
        """ ---- """
        if self.path == '/':
            self.path = '/ourService.html'
        return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

Handler = MyRequestHandler
server = SocketServer.TCPServer(('0.0.0.0', 8954), Handler)

print 'Started my REST API on port 8954' 
server.serve_forever()
