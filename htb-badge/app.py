from flask import Flask, jsonify, send_file
import requests

app = Flask(__name__)

HTB_USER_ID = "ifeelkiddo"  # Replace this with your ID

@app.route('/htb-badge')
def htb_badge():
    url = f"https://app.hackthebox.com/api/v4/profile/{HTB_USER_ID}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        user = data.get("info", {})
        return jsonify({
            "name": user.get("name", "Unknown"),
            "rank": user.get("rank", {}).get("name", "Unranked"),
            "points": user.get("points", 0),
            "respect": user.get("respect", 0)
        })
    return jsonify({"error": "Failed to fetch profile"}), 500
