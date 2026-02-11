from http.server import BaseHTTPRequestHandler
import json
import urllib.request

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.run_logic()
        
    def do_POST(self):
        # Game එක එවපු POST දත්ත කියවා අවසන් කිරීම (Error එක නතර කිරීමට)
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            if content_length > 0:
                self.rfile.read(content_length)
        except:
            pass
        self.run_logic()

    def run_logic(self):
        try:
            # Garena එකේ ඇත්තම දත්ත ගැනීම
            smeta_url = "https://version.freefire.info/public/smeta"
            req = urllib.request.Request(smeta_url, headers={'User-Agent': 'Mozilla/5.0'})
            
            with urllib.request.urlopen(req) as response:
                garena_data = json.loads(response.read().decode())

            # දත්ත සකස් කිරීම
            garena_data["s_url"] = "https://authsrv.astutech.online/"
            garena_data["server_url"] = "https://authsrv.astutech.online/"
            garena_data["status"] = "success"

            # නිවැරදි Headers යැවීම
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            self.wfile.write(json.dumps(garena_data).encode('utf-8'))

        except Exception as e:
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "success", "info": "Navii Fix"}).encode('utf-8'))
