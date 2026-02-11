from http.server import BaseHTTPRequestHandler
import json
import urllib.request

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.handle_all()

    def do_POST(self):
        self.handle_all()

    def handle_all(self):
        try:
            # 1. Garena smeta එක ලබා ගැනීම
            smeta_url = "https://version.freefire.info/public/smeta"
            headers = {'User-Agent': 'okhttp/4.9.1'} # APK එකේ පාවිච්චි කරන version එක
            
            req = urllib.request.Request(smeta_url, headers=headers)
            with urllib.request.urlopen(req) as response:
                content = response.read().decode('utf-8')
                data = json.loads(content)

            # 2. IOS Script එකේ සහ APK එකේ Logic එක අනුව සකස් කිරීම
            # මෙතන s_url එක සහ server_url එක දෙකම දිය යුතුයි
            data["s_url"] = "https://authsrv.astutech.online/"
            data["server_url"] = "https://authsrv.astutech.online/"
            data["status"] = "success"

            # 3. Game එකට අවශ්‍ය නිවැරදි response එක යැවීම
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Connection', 'keep-alive')
            self.end_headers()
            
            self.wfile.write(json.dumps(data).encode('utf-8'))

        except Exception as e:
            # Error එකක් ආවොත් සරල success message එකක් යවනවා app එක crash නොවී ඉන්න
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            err_data = {"status": "success", "server_url": "https://authsrv.astutech.online/"}
            self.wfile.write(json.dumps(err_data).encode('utf-8'))
