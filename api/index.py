from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self._send_response()

    def do_POST(self):
        # Game එක එවන දත්ත කියවන්න ඕනේ, නැත්නම් Game එක Error දෙනවා
        content_length = int(self.headers.get('Content-Length', 0))
        if content_length > 0:
            post_data = self.rfile.read(content_length)
        
        self._send_response()

    def _send_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        # Game එකට තේරෙන භාෂාවෙන් (Structure එකෙන්) දත්ත යවමු
        # "code": 0 කියන්නේ Success කියන එකයි.
        response_data = {
            "code": 0,
            "msg": "success",
            "data": {
                "uid": "100000001",
                "token": "access_token_navii",
                "name": "Navii",
                "level": 100,
                "rank": "Grandmaster",
                "gems": 999999,
                "gold": 999999,
                "is_guest": False
            }
        }
        
        self.wfile.write(json.dumps(response_data).encode())
