import BaseHTTPServer
import ssl
import socket
import json


class HTTPServerV6(BaseHTTPServer.HTTPServer):
  address_family = socket.AF_INET6

TYPES_RESPONSE = '{"status":"Success","data":{"resultCount":10, "indicatorType": []}}'

class S(BaseHTTPServer.BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        path = self.path
        print("incomming http: ", path)
        if '/v2/types' in path:
            json.loads(TYPES_RESPONSE)
            self.wfile.write(TYPES_RESPONSE)
        if '/v2/owners' in path:
            self.wfile.write('{"status":"Success","data":{"resultCount":2,"owner":[{"id":0,"name":"Exemplary Organization","type":"Organization"},{"id":1,"name":"Common Community","type":"Community"}]}}')

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write("<html><body><h1>POST!</h1></body></html>")

httpd = HTTPServerV6(('localhost', 4443), S)
httpd.socket = ssl.wrap_socket(httpd.socket, certfile='./server.pem', server_side=True)
httpd.serve_forever()
