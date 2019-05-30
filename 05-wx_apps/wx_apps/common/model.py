# -*- coding:utf-8 -*-
# author:HPCM
# datetime:2019/5/29 10:45
import os
import base64
from hashlib import sha256
from datetime import datetime

from application import db


class User(db.Model):
    """用户表"""
    __tablename__ = "user"
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True, comment="id")
    nickname = db.Column(db.String(64), default="", nullable=False, comment="昵称")
    mobile = db.Column(db.String(16), default="", nullable=False, comment="手机号")
    email = db.Column(db.String(64), default="", nullable=False, comment="邮箱")
    sex = db.Column(db.Boolean, default=1, nullable=False, comment="性别: 女(0)/男(1)")
    avatar = db.Column(db.String(64), nullable=False, default="", comment="头像")
    username = db.Column(db.String(32), nullable=False, unique=True, comment="登录账号")
    _password = db.Column("password", db.String(128), nullable=False, comment="登录密码")
    salt = db.Column(db.String(64), nullable=False, comment="盐")
    status = db.Column(db.Boolean, nullable=False, default=1, comment="账户状态: 无效(0)/有效(1)")
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now, comment="账号创建时间")
    update_time = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now,
                            comment="最后一次登录时间")

    def to_dict(self):
        """序列化"""
        return {
            "nickname": self.nickname,
            "mobile": self.mobile,
            "email": self.email,
            "sex": self.sex,
            "avatar": self.avatar,
            "account": self.account,
            "password": self.password,
            "salt": self.salt,
            "status": self.status,
            "create_time": self.create_time,
            "update_time": self.update_time
        }

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        """设置密码"""
        self.salt = bytes.decode(base64.b64encode(os.urandom(32)))
        hash_str = self.__hash_password(password, self.salt)
        self._password = hash_str

    @staticmethod
    def __hash_password(password, salt):
        """密码加密"""
        s = sha256("{}{}".format(password, salt).encode())
        hash_pwd_salt = s.hexdigest()
        return "sha256-{}".format(hash_pwd_salt)

    def check_password(self, password):
        """密码比较"""
        if not password:
            return False
        test_str = self.__hash_password(password, self.salt)
        if test_str != self.password:
            return False
        else:
            return True
