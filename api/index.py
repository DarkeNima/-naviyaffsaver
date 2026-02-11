from http.server import BaseHTTPRequestHandler
import urllib.request
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.proxy_request()

    def do_POST(self):
        self.proxy_request()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def proxy_request(self):
        # අපි සම්බන්ධ වෙන්න ඕනේ ඇත්තම Garena Version Server එක
        target_url = "https://versions.garenanow.live/live" + self.path
        
        try:
            # Game එකෙන් එන Request එක ඇත්තම සර්වර් එකට යැවීම
            req = urllib.request.Request(target_url, method=self.command)
            
            # POST Request එකක් නම් එහි දත්ත ලබා ගැනීම
            content_length = int(self.headers.get('Content-Length', 0))
            if content_length > 0:
                data = self.rfile.read(content_length)
                req.data = data
            
            # headers පිටපත් කිරීම
            for key, value in self.headers.items():
                if key.lower() not in ['host', 'content-length']:
                    req.add_header(key, value)

            # ඇත්තම සර්වර් එකෙන් ලැබෙන පිළිතුර කියවීම
            with urllib.request.urlopen(req) as response:
                self.send_response(response.status)
                
                # Headers යැවීම
                for key, value in response.getheaders():
                    self.send_header(key, value)
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                
                # දත්ත ටික Game එකට යැවීම
                self.wfile.write(response.read())

        except Exception as e:
            # කිසියම් දෝෂයක් ආවොත් සරල සාර්ථක පිළිතුරක් යැවීම (Backup)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            backup_data = {"status": "success", "message": "Proxy Active"}
            self.wfile.write(json.dumps(backup_data).encode())
