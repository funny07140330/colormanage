from flask import render_template, request,redirect,jsonify,session
from app_config import app
import requests
import os
from models import User, db
from flask_cors import CORS

BASE_DIR = os.path.join(os.getcwd(), 'static', 'uploads') #用户上传的总目录
print(BASE_DIR)

CORS(app)


@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/page2/')
def page2():
    return render_template('page2.html')

@app.route('/page3/')
def page3():
    return render_template('page3.html')

@app.route('/login/',methods=['POST','GET'])
def login():
    if request.method=="POST":
        username = request.form.get('username')
        result = db.session.query(User).filter_by(username=username)
        if result:
            try:
                password = request.form.get('password')
                if result.first().password == password:
                    session['user_id'] = result.first().id #找到登陆人
                    return jsonify({'data':'登陆成功！','code':200})
                else:
                    return jsonify({'data': '登陆失败！密码错误！', 'code': 204})
            except:
                return jsonify({'data': '该用户不存在！', 'code': 204})
    else:
        return render_template('login.html')
@app.route('/logout/',methods=['POST','GET'])
def logout():
    del session['user_id']
    return redirect('/login/')
if __name__ == "__main__": #程序入口
    app.run(port=8388, debug=True)
