#-*- coding: UTF-8 -*-
from flask import Flask
from flask import render_template
from codes import common
from codes.Settings import SECRET_KEY

app = Flask(__name__)
app.debug = True

#会话密钥
app.secret_key = SECRET_KEY

@app.route('/')
def Login():
	return render_template('login.html',content=common.DoubanAuth())

@app.route('/auth')
def Logined():
	return render_template('auth.html',content=common.DoumaoAuth())

if __name__ == '__main__':
    app.run(debug=True)