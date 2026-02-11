from http.server import BaseHTTPRequestHandler
import json
import urllib.request

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_final_response()

    def do_POST(self):
        # Game එකෙන් එන දත්ත කියවා අවසන් කිරීම (Vercel crash වීම වැළැක්වීමට)
        content_length = int(self.headers.get('Content-Length', 0))
        if content_length > 0:
            self.rfile.read(content_length)
        self.send_final_response()

    def send_final_response(self):
        try:
            # 1. Garena නිල දත්ත ලබා ගැනීම
            smeta_url = "https://version.freefire.info/public/smeta"
            req = urllib.request.Request(smeta_url, headers={'User-Agent': 'okhttp/4.9.1'})
            
            with urllib.request.urlopen(req) as response:
                garena_data = json.loads(response.read().decode('utf-8'))

            # 2. iOS Script එකේ logic එක අනුව දත්ත සැකසීම
            # Astutech සර්වර් එකට සම්බන්ධ වීමට අවශ්‍ය දත්ත
            garena_data["s_url"] = "https://authsrv.astutech.online/"
            garena_data["server_url"] = "https://authsrv.astutech.online/"
            garena_data["status"] = "success"

            # 3. Vercel එකෙන් දත්ත යවන විදිහ (මෙතන තමයි වෙනස තියෙන්නේ)
            response_body = json.dumps(garena_data, ensure_ascii=False).encode('utf-8')

            self.send_response(200)
            # Headers ඉතාම නිවැරදිව ලබා දීම
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Content-Length', str(len(response_body)))
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            self.wfile.write(response_body)

        except Exception:
            # කිසියම් දෝෂයක් වුවහොත් සරල Response එකක් දීම
            fallback = {"status": "success", "server_url": "https://authsrv.astutech.online/"}
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(fallback).encode('utf-8'))
