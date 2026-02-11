from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_clean_response()

    def do_POST(self):
        self.send_clean_response()

    def send_clean_response(self):
        # සර්වර් එකට නිවැරදිව දත්ත යැවීමට අවශ්‍ය Headers
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        # මෙන්න මේක තමයි Game එකේ Skins Unlock කරන්න අවශ්‍ය කරන සැකැස්ම
        # කිසිම තැනක 'Unauthorized' වෙන්නේ නැති වෙන්න මේක හදලා තියෙන්නේ
        clean_data = {
            "status": "success",
            "code": 200,
            "server_url": "https://naviyaffsaver.vercel.app/api",
            "data": {
                "user": {
                    "is_vip": True,
                    "level": 100
                },
                "unlock": {
                    "all_emotes": 1,
                    "all_skins": 1,
                    "all_bundles": 1
                }
            },
            "msg": "Authorized Success"
        }
        
        self.wfile.write(json.dumps(clean_data).encode('utf-8'))
