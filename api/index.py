from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.redirect_to_astute()

    def do_POST(self):
        self.redirect_to_astute()

    def redirect_to_astute(self):
        # අපි කෙලින්ම Astutech එකේ වැඩ කරන URL එකකට Redirect කරනවා
        # මෙතන /auth හෝ /version වගේ path එකක් අනුමාන කරලා තියෙන්නේ
        target = "https://authsrv.astutech.online" + self.path
        
        self.send_response(301) # Permanent Redirect
        self.send_header('Location', target)
        self.end_headers()
