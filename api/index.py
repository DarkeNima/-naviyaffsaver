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
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        # ගොඩක් සර්වර් වල සාර්ථක පිළිතුරක් ලැබෙන්නේ මේ සරල ආකාරයටයි
        response_data = {
            "status": 0,
            "message": "success",
            "data": {
                "gems": 999999,
                "gold": 999999,
                "diamond": 999999,
                "level": 100,
                "exp": 999999,
                "vip": 10
            }
        }
        
        self.wfile.write(json.dumps(response_data).encode())
