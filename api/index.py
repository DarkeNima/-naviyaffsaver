from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.handle_all()

    def do_POST(self):
        # Game එක එවන්න ඕනෑම දත්තයක් (Body) කියවා අවසන් කිරීම
        content_length = int(self.headers.get('Content-Length', 0))
        if content_length > 0:
            self.rfile.read(content_length)
        self.handle_all()

    def handle_all(self):
        # Game එක බලාපොරොත්තු වන නිවැරදි Headers
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        # මෙන්න මේක තමයි Astutech සර්වර් එකෙන් යවන රහස් දත්ත සැකැස්ම
        # අපි මේක 'Authorized' විදිහට පෙන්වනවා
        response = {
            "status": "success",
            "auth": True,
            "server_url": "https://authsrv.astutech.online/",
            "data": {
                "user_info": {"id": "12345", "vip": 1},
                "unlocks": ["all_emotes", "all_skins", "all_bundles"],
                "config": {"bypass": True}
            }
        }
        
        self.wfile.write(json.dumps(response).encode('utf-8'))
