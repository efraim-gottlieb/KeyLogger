from flask import Flask, jsonify, request, send_from_directory
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# בסיס הנתיב: איפה שהקובץ server.py יושב
BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))

# תיקיות יחסיות
DEVICES_FOLDER = os.path.join(BASE_FOLDER, "data", "devices")
FRONTEND_FOLDER = os.path.join(BASE_FOLDER, "frontend")

users = {'kodcode': '2025'}

@app.route('/')
def home():
    return send_from_directory(FRONTEND_FOLDER, 'login.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users and users[username] == password:
        return jsonify({"success": True})
    else:
        return jsonify({"success": False})

@app.route('/computers', methods=['GET'])
def list_computers():
    try:
        if not os.path.exists(DEVICES_FOLDER):
            return jsonify({"error": "Devices folder not found"}), 404

        computers = [d for d in os.listdir(DEVICES_FOLDER)]
        return jsonify({"computers": computers})

    except Exception as e:
        # שגיאה מבוקרת במקום דף HTML
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
