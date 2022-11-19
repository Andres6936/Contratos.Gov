import http.server
import json
from http.server import BaseHTTPRequestHandler

from Scraper.Logger.GeneralMessage import GeneralMessage
from Scraper.Parser.JSONParser import JSON

hostName = "localhost"
serverPort = 8080


def auth(user: JSON) -> JSON:
    return user


class SimpleServer(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/auth":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            contentLength = int(self.headers.get('Content-Length'))
            response = auth(user=json.loads(self.rfile.read(contentLength)))
            self.wfile.write(json.dumps(response).encode("utf-8"))
        else:
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"name": "admin"}).encode("utf-8"))


def main():
    with http.server.HTTPServer((hostName, serverPort), SimpleServer) as httpd:
        GeneralMessage.publish(f"Running Web Server in https://{hostName}:{serverPort}")
        httpd.serve_forever()
    GeneralMessage.publish("Server Stopped")
