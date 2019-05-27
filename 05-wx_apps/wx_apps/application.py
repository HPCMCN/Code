#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Power by HPCM 2019-05-27 10:12:16
# Filename application.py
from flask import Flask
from flask_script import Manager, Command
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy


class Application(object):
    def __init__(self):
        self.app = Flask(__name__)
        self.model = None
        self.db = None

    def config(self):
        """配置flask"""
        from config import constants
        self.app.config.from_object(constants.Config(self.model))

    def register(self):
        """蓝图注册"""
        from apps.users.view import bp_user
        self.app.register_blueprint(bp_user)

    def run(self, model, host=None, port=None):
        """系统启动器"""
        self.model = model
        self.config()
        self.register()
        self.app.run(host, port)

    def manager(self):
        """app托管"""
        Migrate(self.app, self.db)
        manager = Manager(self.app)
        manager.add_command("db", MigrateCommand)
        return manager


apps = Application()
app = apps.app