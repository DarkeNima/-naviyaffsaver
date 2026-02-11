from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self._send_response()

    def do_POST(self):
        self._send_response()

    def _send_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        # මේක දාන්න ඕනේ Game එකට දත්ත කියවන්න ඉඩ දෙන්න
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        data = {
            "status": "success",
            "gems": 999999,
            "gold": 999999,
            "level": 100,
            "rank": "Grandmaster",
            "unlocked_all": True,
            "message": "Welcome Navii! Your Private Server is Active."
        }
        
        self.wfile.write(json.dumps(data).encode())
