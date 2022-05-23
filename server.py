from http.server import  HTTPServer,BaseHTTPRequestHandler
PORT = 8000
HOST="192.168.206.66"

class NeuralHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
          self.send_response((200))
          self.send_header("Content-type","text/html")
          self.end_headers()
          self.wfile.write(bytes("<html><body> <h1>Zigler</h1></body></html>","utf-8"))




server=HTTPServer((HOST,PORT),NeuralHTTP)
print("server running...")
server.serve_forever()
