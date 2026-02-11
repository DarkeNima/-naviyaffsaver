from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.respond_with_data()

    def do_POST(self):
        self.respond_with_data()

    def respond_with_data(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        # Astutech Script එකේ තිබුණු විදිහටම සකස් කළ දත්ත
        # මෙන්න මේ structure එක තමයි Skins/Emotes unlock කරන්න උදව් වෙන්නේ
        response_data = {
            "s_url": "https://authsrv.astutech.online/",
            "server_url": "https://authsrv.astutech.online/",
            "status": "success",
            "vh": ["versions.garenanow.live", "naviyaffsaver.vercel.app"],
            "data": {
                "unlock_all": True,
                "emotes": "active",
                "kits": "active",
                "skins": "active"
            }
        }
        
        self.wfile.write(json.dumps(response_data).encode('utf-8'))
