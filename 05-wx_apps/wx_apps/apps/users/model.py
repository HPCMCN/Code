# -*- coding:utf-8 -*-
# author:HPCM
# datetime:2019/5/29 10:45
from datetime import datetime

from application import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True, comment="id")
    nickname = db.Column(db.String(64), nullable=False, comment="用户名")
    mobile = db.Column(db.String(16), nullable=False, comment="手机号")
    email = db.Column(db.String(64), nullable=False, comment="邮箱")
    sex = db.Column(db.Boolean, default=1, nullable=False, comment="性别: 女(0)/男(1)")
    avatar = db.Column(db.String(64), nullable=False, comment="头像")
    account = db.Column(db.String(32), nullable=False, unique=True, comment="登录账号")
    password = db.Column(db.String(32), nullable=False, comment="登录密码")
    salt = db.Column(db.String(32), nullable=False, comment="盐")
    status = db.Column(db.Boolean, nullable=False, comment="账户状态: 无效(0)/有效(1)")
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now, comment="账号创建时间")
    update_time = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now, comment="最后一次登录时间")
