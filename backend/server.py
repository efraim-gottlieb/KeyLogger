
from flask import Flask, jsonify, request

app=Flask(__name__)
data=''
@app.route('/',methods=['GET'])
def response_data():
    res=f'<h1> סודי ביותר </h1><p1>{data}</p1>'
    return res

@app.route('/post',methods=['POST'])
def requests_data():
    global data
    req=request.data
    data +=str(req)
    print(data)
    return 'OK'



if __name__==('__main__'):
    app.run(debug=True)