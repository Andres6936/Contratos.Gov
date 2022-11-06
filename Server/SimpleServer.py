from http.server import BaseHTTPRequestHandler, HTTPServer

from Scraper.GeneralMessage import GeneralMessage

hostName = "localhost"
serverPort = 8080


class SimpleServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))


def main():
    webserver = HTTPServer((hostName, serverPort), SimpleServer)
    GeneralMessage.publish(f"Running Web Server in https://{hostName}:{serverPort}")
    try:
        webserver.serve_forever()
    except KeyboardInterrupt:
        pass

    webserver.server_close()
    GeneralMessage.publish("Server Stopped")
