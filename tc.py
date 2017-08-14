import BaseHTTPServer
import ssl
import socket
import json


class HTTPServerV6(BaseHTTPServer.HTTPServer):
  address_family = socket.AF_INET6

TYPES_RESPONSE = '{"status":"Success","data":{"resultCount":10, "indicatorType": [{"name": "File","custom": "false","apiEntity": "file"}]}}'

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
        if '/v2/indicators/files' in path:
            self.wfile.write('{"status":"Success","data":{"file":{"id":90558,"owner":{"id":1,"name":"System","type":"Organization"},"dateAdded":"2015-07-06T11:09:33-04:00","lastModified":"2015-07-06T11:09:33-04:00","rating":4,"confidence":70,"webLink":"null/auth/indicators/details/file.xhtml?file=422AD421127685E3EF4A44B546258107&owner=System","source":"foosource","description":"foodescription","md5":"422AD421127685E3EF4A44B546258107","sha1":"6EE03D201FE358139858956383F3C280ACADEB8E","sha256":"DFB94E30E5764527501B3232E237199BE33756612A0D1284EAB191EB6CE405D6","size":1663}}}')

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write("<html><body><h1>POST!</h1></body></html>")

httpd = HTTPServerV6(('localhost', 4443), S)
httpd.serve_forever()
