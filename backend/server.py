from flask import Flask, jsonify, request, send_from_directory
import os
from flask_cors import CORS
app=Flask(__name__)
CORS(app)
data=''

BASE_FOLDER = os.getcwd()
DEVICES_FOLDER = os.path.join(BASE_FOLDER, "data", "devices")
FRONTEND_FOLDER = os.path.join(os.getcwd(), "frontend")

users = {'admin' : '123'}

@app.route('/')
def home():
    return send_from_directory(FRONTEND_FOLDER, "login.html")

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users and users[username] == password:
        return jsonify({"success": True})
    else:
        return jsonify({"success":False})

@app.route('/computers', methods=['GET'])
def list_computers():
    computers = [d for d in os.listdir(DEVICES_FOLDER)]

    return {"computers": computers}



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)