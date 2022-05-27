from http.server import HTTPServer, CGIHTTPRequestHandler


server_address = ("", 8000)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
print(httpd.get_request())
httpd.serve_forever()
