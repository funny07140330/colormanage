#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__,
template_folder='templates',
static_folder='static',)  #找到静态文件
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/test2021'#链接数据库
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True  #链接数据库
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True#链接数据库
app.config['SECRET_KEY'] = '!@!@@#@#@#$#SWE##@1231231231' #session加密
