from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.handle_all()

    def do_POST(self):
        self.handle_all()

    def do_OPTIONS(self):
        self.handle_all()

    def handle_all(self):
        # Game එකට අවශ්‍ය කරන Headers සකස් කිරීම
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

        # මෙන්න මේ දත්ත ටික තමයි Game එකේ Dashboard එකට අවශ්‍ය වෙන්නේ
        response_data = {
            "code": 200,
            "status": "success",
            "message": "Connected to Navii Server",
            "data": {
                "user_info": {
                    "nickname": "Navii_VIP",
                    "level": 100,
                    "exp": 999999,
                    "rank_name": "Grandmaster"
                },
                "inventory": {
                    "diamonds": 999999,
                    "gold": 999999,
                    "gems": 999999
                },
                "settings": {
                    "is_unlocked": True,
                    "no_ads": True
                }
            }
        }
        
        self.wfile.write(json.dumps(response_data).encode('utf-8'))
