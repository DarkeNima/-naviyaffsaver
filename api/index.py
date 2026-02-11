from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self._set_headers()
        self.wfile.write(json.dumps(self._get_data()).encode('utf-8'))

    def do_POST(self):
        self._set_headers()
        self.wfile.write(json.dumps(self._get_data()).encode('utf-8'))

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def _get_data(self):
        return {
            "status": 0,
            "error": 0,
            "access_token": "navii_secret_token_777",
            "data": {
                "gems": 999999,
                "gold": 999999,
                "level": 100,
                "rank": "Grandmaster"
            }
        }
