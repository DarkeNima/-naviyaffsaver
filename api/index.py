from http.server import BaseHTTPRequestHandler
import json
import urllib.request

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.handle_request()

    def do_POST(self):
        self.handle_request()

    def handle_request(self):
        try:
            # 1. Garena එකේ ඇත්තම Meta දත්ත (smeta) ලබා ගැනීම
            smeta_url = "https://version.freefire.info/public/smeta"
            with urllib.request.urlopen(smeta_url) as response:
                garena_data = json.loads(response.read().decode())

            # 2. ඔයා එවපු Script එකේ Logic එක: 
            # ඇත්තම දත්ත වලට 'server_url' එක එකතු කිරීම
            # මෙතනට අපි දෙන්නේ ඇත්තම Astutech සර්වර් එකේ ලින්ක් එක
            garena_data["server_url"] = "https://authsrv.astutech.online/"
            
            # 3. Game එකට දත්ත යැවීම
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            self.wfile.write(json.dumps(garena_data).encode('utf-8'))

        except Exception as e:
            # මොනවා හරි වැරදුනොත් Backup එකක් දීම
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error_resp = {"server_url": "https://authsrv.astutech.online/", "status": "ok"}
            self.wfile.write(json.dumps(error_resp).encode('utf-8'))
