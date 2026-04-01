from http.server import BaseHTTPRequestHandler, HTTPServer
import ssl

HOST = "127.0.0.1"
PORT = 8443

HTML = b"""<!doctype html>
<html>
  <head>
    <meta charset="utf-8"/>
    <title>RealBank - Clone (HTTPS)</title>
  </head>
  <body>
    <h1>REALBANK (CLONE) - HTTPS</h1>
    <p><b>Demo:</b> This uses a self-signed certificate.</p>
    <p>A real browser should warn: untrusted issuer / possible mismatch.</p>
    <p><small>Demo domain: realbank.test</small></p>
  </body>
</html>
"""


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(HTML)))
        self.end_headers()
        self.wfile.write(HTML)

    def log_message(self, fmt, *args):
        print(f"[EVIL-HTTPS] {self.client_address[0]}:{self.client_address[1]} - {fmt % args}")


def main():
    httpd = HTTPServer((HOST, PORT), Handler)

    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

    print(f"Evil HTTPS server running on https://{HOST}:{PORT}")
    httpd.serve_forever()


if __name__ == "__main__":
    main()
