from http.server import BaseHTTPRequestHandler
import json
import urllib.request

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.handle_proxy()

    def do_POST(self):
        self.handle_proxy()

    def handle_proxy(self):
        try:
            # 1. ඇත්තම Garena Meta දත්ත ලබා ගැනීම
            with urllib.request.urlopen("https://version.freefire.info/public/smeta") as response:
                meta_data = json.loads(response.read().decode())

            # 2. Game එකට අවශ්‍ය කරන නිවැරදි Response එක සකස් කිරීම
            # මෙතන 'server_url' එක තමයි වැදගත්ම දේ
            result = {
                "server_url": meta_data.get("s_url", "https://authsrv.astutech.online/"),
                "status": "success",
                "version": "1.100.x",
                "patch": "active"
            }

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            self.wfile.write(json.dumps(result).encode())

        except Exception as e:
            # මොනවා හරි වැරදුනොත් Backup එකක් විදිහට මේක යවනවා
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"server_url": "https://authsrv.astutech.online/"}).encode())
