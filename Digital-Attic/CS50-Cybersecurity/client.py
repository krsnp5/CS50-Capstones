from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = "127.0.0.1"
PORT = 8001

HTML = b"""<!doctype html>
<html>
  <head>
    <meta charset="utf-8"/>
    <title>RealBank - Clone</title>
  </head>
  <body>
    <h1>REALBANK (CLONE)</h1>
    <p><b>WARNING (for the demo):</b> This is the lookalike site.</p>
    <p>This simulates what a victim might see after DNS redirection.</p>
    <form>
      <label>Password: <input type="password" placeholder="do not enter real passwords"></label>
      <button type="button">Sign in</button>
    </form>
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
        print(f"[EVIL ] {self.client_address[0]}:{self.client_address[1]} - {fmt % args}")


def main():
    print(f"Evil server running on http://{HOST}:{PORT}")
    HTTPServer((HOST, PORT), Handler).serve_forever()


if __name__ == "__main__":
    main()
