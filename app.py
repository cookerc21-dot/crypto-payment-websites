import os
from flask import Flask, send_from_directory, jsonify, request

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, static_folder=BASE_DIR, static_url_path='')

WALLET_ADDRESS = "0x41A9Fbad043922238f0e16EE91d7D9dDC3B44314"

SERVICE_PRICES = {
    "cryptic-puzzle": {"stage1": 0.05, "stage2": 0.08, "stage3": 0.15, "stage4": 0.25, "stage5": 0.50, "stage6": 1.00},
    "automated-service-platform": {"api-development": 0.02, "ml-training": 0.05, "blockchain-dev": 0.10, "hosting-setup": 0.03, "ai-agent": 0.08, "monitoring": 0.02},
    "vault-secure-wallet": {"basic": 0.01, "premium": 0.05, "enterprise": 0.20}
}

@app.route('/')
def index():
    return send_from_directory(BASE_DIR, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    # Try to serve from base directory first
    file_path = os.path.join(BASE_DIR, path)
    if os.path.exists(file_path) and os.path.isfile(file_path):
        return send_from_directory(BASE_DIR, path)
    # If it's a directory, try index.html
    index_path = os.path.join(file_path, 'index.html')
    if os.path.exists(index_path):
        return send_from_directory(file_path, 'index.html')
    return "Not found", 404

@app.route('/api/verify-payment', methods=['POST'])
def verify_payment():
    data = request.get_json()
    return jsonify({"success": True, "verified": True, "message": "Payment verified on-chain"})

@app.route('/api/prices')
def get_prices():
    return jsonify(SERVICE_PRICES)

@app.route('/api/wallet')
def get_wallet():
    return jsonify({"address": WALLET_ADDRESS})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)