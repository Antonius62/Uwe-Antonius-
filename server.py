from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl

server_address = ('0.0.0.0', 8443)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

# SSL-Kontext erstellen
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain('cert.pem', 'key.pem')
httpd.socket = ssl_context.wrap_socket(httpd.socket, server_side=True)

print('Server läuft auf https://localhost:8443')
httpd.serve_forever()
