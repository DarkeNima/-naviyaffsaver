from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.respond()

    def do_POST(self):
        # Game එක එවන දත්ත කියවා ඉවත් කිරීම (වැදගත්)
        content_length = int(self.headers.get('Content-Length', 0))
        if content_length > 0:
            self.rfile.read(content_length)
        self.respond()

    def respond(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        # Login Failed: 4 දෝෂය මඟහරින නිවැරදි දත්ත සැකැස්ම
        data = {
            "error": 0,
            "access_token": "navii_vip_token_12345",
            "open_id": "123456789",
            "expires_in": 360000,
            "user_info": {
                "name": "Navii",
                "gems": 999999,
                "gold": 999999,
                "level": 100
            }
        }
        
        self.wfile.write(json.dumps(data).encode())
