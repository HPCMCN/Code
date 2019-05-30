#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Power by HPCM 2019-05-27 10:12:16
# Filename application.py
import os
import logging.config

from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# noinspection PyProtectedMember,PyUnboundLocalVariable
class Application(object):
    def __init__(self):
        self.app = Flask(__name__)
        self.base_dir = None

    def config(self):
        """配置flask"""
        from config import constants
        from common import url_manager
        self.app.config.from_object(constants.Config())
        logging.config.dictConfig(self.app.config.get("LOGGER"))
        db.init_app(self.app)
        self.app.add_template_global(url_manager.build_url, "buildUrl")
        self.app.add_template_global(url_manager.build_static_url, "buildStaticUrl")
        self.app.template_folder = os.path.join(self.base_dir, "templates")
        self.app.static_folder = os.path.join(self.base_dir, "static")
        self.app.root_path = self.base_dir

    def register(self):
        """蓝图注册"""
        from apps.users.view import bp_user
        from apps.index.view import bp_index
        from apps.account.view import bp_account
        from apps.vip.view import bp_vip
        from apps.food.view import bp_food
        from apps.finance.view import bp_finance
        from apps.stat.view import bp_stat
        from apps.error.view import bp_error
        self.app.register_blueprint(bp_user)
        self.app.register_blueprint(bp_index)
        self.app.register_blueprint(bp_account)
        self.app.register_blueprint(bp_vip)
        self.app.register_blueprint(bp_food)
        self.app.register_blueprint(bp_finance)
        self.app.register_blueprint(bp_stat)
        self.app.register_blueprint(bp_error)

    def start(self):
        """系统启动器"""
        self.config()
        self.register()
        manager = self.manager()
        manager.run()

    def set_base_dir(self, base_dir):
        """设置BASE_DIR"""
        self.base_dir = base_dir

    def manager(self):
        """初始化托管程序"""
        manager = Manager(self.app)
        self.manager_db(manager)
        self.manager_account(manager)
        return manager

    def manager_db(self, manager):
        """数据库托管"""
        Migrate(self.app, db)
        manager.add_command("db", MigrateCommand)

    @staticmethod
    def manager_account(manager):
        """账号密码插入"""

        @manager.command
        def create_user():
            """创建用户账号"""
            from common.model import User
            user = User()
            for _ in range(3):
                username = input("请输入登录账号:\n")
                if not User.query.filter_by(username=username).all():
                    break
            else:
                print("重试次数超限!")
                exit(0)
            user.username = username
            user.password = input("请输入登录密码:\n")
            user.nickname = user.username
            db.session.add(user)
            db.session.commit()
            print("用户: {} 创建成功!".format(user.nickname))


apps = Application()
app = apps.app
