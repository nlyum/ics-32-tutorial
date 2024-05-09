#
# Simple server that only understands POST
#
import http
import http.server
import socketserver


class ICSHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """
    This is a subclass of the BaseHTTPRequestHandler class which provides
    methods for various aspects of HTTP request management.
    """
    def do_POST(self):
        # Defines what to do when a POST is received by the server
        # Prints the command that was received
        print(self.command + " received.")
        # Read the amount of data specified in the headers
        data = self.rfile.read(int(self.headers['content-length']))
        # Prepares and send the reply to the client
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write("ok".encode(encoding = 'utf-8'))
        # Prints the received data by the server to the server screen
        print(data.decode(encoding = 'utf-8'))


if __name__ == "__main__":
    PORT = 8000
    # Instantiates a TCP server that uses the HTTP handler (thus a webserver!)
    simple_server = socketserver.TCPServer(("", PORT),
                                           ICSHTTPRequestHandler)
    print ("Simple server listening to POST serving at port", PORT)
    # Starts the server
    simple_server.serve_forever()
