from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.respond()
    def do_POST(self):
        self.respond()

    def respond(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        # Astutech සර්වර් එකේ වගේ Skin/Emote Config එකක්
        config_data = {
            "status": "success",
            "data": {
                "user": {"name": "Navii_VIP", "level": 100},
                "unlock_config": {
                    "all_skins": True,
                    "all_emotes": True,
                    "all_bundles": True,
                    "anti_ban": True
                },
                "items": [
                    {"id": "101", "name": "Sakura Bundle", "status": 1},
                    {"id": "201", "name": "Hip Hop Bundle", "status": 1},
                    {"id": "501", "name": "Flag Emote", "status": 1}
                ],
                "server_key": "active_session_navii_777"
            },
            "config": {
                "show_skins_to_user": True,
                "enable_mods": True
            }
        }
        self.wfile.write(json.dumps(config_data).encode())
