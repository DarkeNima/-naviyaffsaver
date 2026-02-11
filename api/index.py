from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.respond()
    def do_POST(self):
        self.respond()

    def respond(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        # FF Game එක සාමාන්‍යයෙන් බලාපොරොත්තු වන Master Data Format එක
        master_data = {
            "code": 0,
            "msg": "success",
            "data": {
                "diamond": 999999,
                "gold": 999999,
                "gem": 999999,
                "cash": 999999,
                "level": 100,
                "rank": 99,
                "badge": 999,
                "exp": 999999
            },
            "status": 200
        }
        self.wfile.write(json.dumps(master_data).encode())
