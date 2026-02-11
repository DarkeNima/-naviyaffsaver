from http.server import BaseHTTPRequestHandler
import urllib.request

class handler(BaseHTTPRequestHandler):
    def handle_request(self):
        # Original Astutech server eke URL eka
        target_url = "https://authsrv.astutech.online" + self.path
        
        # Game eken ena headers kiyawaa ganeema
        headers = {key: value for key, value in self.headers.items() if key.lower() != 'host'}
        
        # POST daththa thibe nam ewa kiyawaa ganeema
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length) if content_length > 0 else None

        try:
            # Original server ekata request eka yawana widiya
            req = urllib.request.Request(target_url, data=post_data, headers=headers, method=self.command)
            with urllib.request.urlopen(req) as response:
                # Original server eken ena daththa (Binary/Encrypted) ehemma labaa ganeema
                res_body = response.read()
                
                # Game ekata pilithura yawana widiya
                self.send_response(response.status)
                for key, value in response.getheaders():
                    self.send_header(key, value)
                self.end_headers()
                self.wfile.write(res_body)
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(str(e).encode())

    def do_GET(self):
        self.handle_request()

    def do_POST(self):
        self.handle_request()
