from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = "127.0.0.1"
PORT = 8000

HTML = b"""<!doctype html>
<html>
  <head>
    <meta charset="utf-8"/>
    <title>RealBank</title>
  </head>
  <body>
    <h1>REALBANK</h1>
    <p>Welcome. This is the legitimate site.</p>
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
        print(f"[LEGIT] {self.client_address[0]}:{self.client_address[1]} - {fmt % args}")


def main():
    print(f"Legit server running on http://{HOST}:{PORT}")
    HTTPServer((HOST, PORT), Handler).serve_forever()


if __name__ == "__main__":
    main()
