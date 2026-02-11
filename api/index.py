from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self._send_response()

    def do_POST(self):
        # POST request එකකදී එන දත්ත කියවා අවසන් කිරීම
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            if content_length > 0:
                self.rfile.read(content_length)
        except:
            pass
        self._send_response()

    def _send_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        # මේක තමයි ගොඩක් FF Saver වල වැඩ කරන Structure එක
        data = {
            "status": 200,
            "message": "success",
            "data": {
                "diamond": 999999,
                "gold": 999999,
                "level": 100,
                "exp": 999999,
                "vip_level": 10,
                "nickname": "Navii_VIP",
                "uid": "12345678"
            },
            "error": 0
        }
        
        self.wfile.write(json.dumps(data).encode('utf-8'))
