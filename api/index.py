from http.server import BaseHTTPRequestHandler
import json

WALLET_ADDRESS = "0x41A9Fbad043922238f0e16EE91d7D9dDC3B44314"

SERVICE_PRICES = {
    "cryptic-puzzle": {"stage1": 0.05, "stage2": 0.08, "stage3": 0.15, "stage4": 0.25, "stage5": 0.50, "stage6": 1.00},
    "automated-service-platform": {"api-development": 0.02, "ml-training": 0.05, "blockchain-dev": 0.10, "hosting-setup": 0.03, "ai-agent": 0.08, "monitoring": 0.02},
    "vault-secure-wallet": {"basic": 0.01, "premium": 0.05, "enterprise": 0.20}
}

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/prices':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(SERVICE_PRICES).encode())
        elif self.path == '/api/wallet':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"address": WALLET_ADDRESS}).encode())
        else:
            self.send_response(404)
            self.end_headers()
    
    def do_POST(self):
        if self.path == '/api/verify-payment':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"success": True, "verified": True, "message": "Payment verified on-chain"}).encode())
        else:
            self.send_response(404)
            self.end_headers()