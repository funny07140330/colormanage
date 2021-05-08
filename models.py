#!/usr/bin/python
# -*- coding: utf-8 -*-
from app_config import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy(app)

# 创建设备1
class User(db.Model):
    __tablename__ = 'userinfo'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(6), nullable=True)
    password = db.Column(db.String(16), nullable=True)
    is_activate = db.Column(db.Integer) #账号是否可用 0不可用 1可用
    can_use_dir = db.Column(db.String(200), nullable=True) #可用文件夹，永不了其他人文件夹
    createTime = db.Column(db.DateTime(timezone=False), server_default=func.now())
    def __repr__(self):
        return '<user %r>' % self.username
