from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/nse/<symbol>")
def get_chain(symbol):
    try:
        url = f"https://www.nseindia.com/api/option-chain-indices?symbol={symbol.upper()}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Accept": "application/json",
            "Referer": "https://www.nseindia.com/"
        }
        r = requests.get(url, headers=headers, timeout=10)
        data = r.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})
        
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
