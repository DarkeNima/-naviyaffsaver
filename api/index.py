from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        # ඔයාට අවශ්‍ය Game Data ටික මෙතන තියෙන්නේ
        # මේ දත්ත වෙනස් කරලා ඔයාට කැමති විදිහට Dashboard එක හදාගන්න පුළුවන්
        game_data = {
            "status": "success",
            "gems": 999999,
            "gold": 999999,
            "level": 100,
            "rank": "Grandmaster",
            "unlocked_all": True,
            "message": "Welcome Navii! Your Private Server is Active."
        }
        
        self.wfile.write(json.dumps(game_data).encode())
        return
