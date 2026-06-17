import json
from http.server import BaseHTTPRequestHandler

WALLET_ADDRESS = "0x41A9Fbad043922238f0e16EE91d7D9dDC3B44314"

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps({"address": WALLET_ADDRESS}).encode())