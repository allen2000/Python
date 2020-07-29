from flask import abort, jsonify, Flask, request, Response, make_response
import json

app = Flask(__name__)
# 增加配置，支持中文显示
app.config['JSON_AS_ASCII'] = False

tasks = {
    "code": 200,
    "status": 1,
    "data": {
        "Address": "192.168.1.999",
        "Version": "V1.00.001",
        "proVersion": "4927",
        "proHttpPort": "7080",
        "SnmpPort": "7090",
        "OtherSnmpPort": "7091",
        "signalingPort": "7092",
        "statusPort": "7093"
    },
    "traceId": "10087"
}

status0 ={
    "code": 200,
    "status": 1,
    "data":{
        "mobile":"9527",
        "password":"123456",
        "role":"SW tester"
    }
}

status1 ={
    "code": 404,
    "status": 0,
    "data":{
        "message":"Can not get the server status"
    }
}
###################以下都是路由########################
@app.route('/')      #相当于一个装饰器，视图映射，路由系统生成 视图对应url，这边没有指定method .默认使用get
def first_flask():    #视图函数
    return "Hello"

@app.route('/status',methods=['post'])
def getstatus():
    data = request.get_json()
    if data.get('status') == 1:
        return jsonify(status0)
    else:
        return jsonify(status1)

@app.route('/hello/<username>',methods=['get'])
def hello(username):
    return "Hello, welcome:"+username

@app.route('/task', methods=['GET'])
def app_call_back():
    if request.method == 'GET':
        return jsonify(tasks)
    else:
        test_data = request.form['params']
        return jsonify(test_data)

@app.route('/login',methods=['get'])
def getlogin():
    mobile=request.args.get('mobile')
    passwd=request.args.get('passwd')
    res =mobile+"---"+passwd
    return res

@app.route('/login1',methods=['post'])
def postformlogin():
    data0 = request.form.get('mobile')
    data1 = request.form.get('passwd')
    return data0+'---'+data1

@app.route('/login2',methods=['post'])
def postjsonlogin():
    data = request.get_json()
    return data.get("mobile")
if __name__ == '__main__':
    app.run(host = '192.168.1.105',debug=True)