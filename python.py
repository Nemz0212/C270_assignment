from http.server import HTTPServer, SimpleHTTPRequestHandler, BaseHTTPRequestHandler

class HTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><body><h1>Hello World!</h1><h2>Python file</h2></body></html>", "utf-8"))



def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    """Entrypoint for python server"""
    HOST = "0.0.0.0"
    PORT = 8000
    httpd = HTTPServer((HOST,PORT), HTTP)

    httpd.serve_forever()


if __name__ == "__main__":
    run()
