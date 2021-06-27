from sys import argv
from urllib.parse import urlsplit, urlunsplit
from http.server import HTTPServer, SimpleHTTPRequestHandler


class BasicServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        (s, n, p, q, f) = urlsplit(self.path)
        if p == "/": p += ENTRY
        if "." not in p: p += ".html"
        self.path = urlunsplit((s, n, p, q, f))
        self.directory = PATH
        return SimpleHTTPRequestHandler.do_GET(self)


PORT = int(argv[1]) if len(argv) >= 2 else 4242
ENTRY = argv[2] if len(argv) >= 3 else "index"
PATH = argv[3] if len(argv) >= 4 else __file__[:-len(argv[0])]

server = HTTPServer(("localhost", PORT), BasicServer)

print(f"Serving the files in {PATH} at http://localhost:{PORT}")

try:
    server.serve_forever()
except KeyboardInterrupt:
    server.server_close()
