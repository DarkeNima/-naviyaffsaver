from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self._send_success()

    def do_POST(self):
        self._send_success()

    def _send_success(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        # මේක තමයි ගොඩක් වෙලාවට වැඩ කරන Universal JSON Structure එක
        response = {
            "status": "success",
            "code": 200,
            "data": {
                "user": {
                    "id": "12345678",
                    "name": "Navii_VIP",
                    "level": 100,
                    "exp": 999999,
                    "rank": 99
                },
                "wallet": {
                    "diamond": 999999,
                    "gold": 999999,
                    "gems": 999999,
                    "credit": 9999
                },
                "token": "navii_session_valid_123"
            }
        }
        
        self.wfile.write(json.dumps(response).encode('utf-8'))
