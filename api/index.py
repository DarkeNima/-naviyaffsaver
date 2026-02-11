from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.handle_request()

    def do_POST(self):
        # Game එක එවන්න පුළුවන් ඕනෑම දත්තයක් කියවා අවසන් කිරීම
        content_length = int(self.headers.get('Content-Length', 0))
        if content_length > 0:
            self.rfile.read(content_length)
        self.handle_request()

    def handle_request(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        # මේ තමයි ගොඩක් Games වල Dashboard එක Unlock කරන 'Master Key' එක
        response = {
            "status": 0,
            "error": 0,
            "message": "success",
            "token": "navii_session_active_999",
            "data": {
                "account": {
                    "uid": "12345678",
                    "nickname": "Navii_VIP",
                    "level": 100,
                    "exp": 9999999,
                    "rank": 99,
                    "is_mod": True
                },
                "wallet": {
                    "gems": 999999,
                    "gold": 999999,
                    "diamond": 999999,
                    "coupon": 9999
                },
                "config": {
                    "bypass_auth": True,
                    "show_ads": False
                }
            }
        }
        
        self.wfile.write(json.dumps(response).encode())
