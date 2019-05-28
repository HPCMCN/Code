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


class Application(object):
    def __init__(self):
        self.app = Flask(__name__)
        self.model = None
        self.base_dir = None

    def config(self):
        """配置flask"""
        from config import constants
        from common import url_manager
        self.app.config.from_object(constants.Config(self.model))
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
        self.app.register_blueprint(bp_user)
        self.app.register_blueprint(bp_index)
        self.app.register_blueprint(bp_account)
        self.app.register_blueprint(bp_vip)
        self.app.register_blueprint(bp_food)
        self.app.register_blueprint(bp_finance)
        self.app.register_blueprint(bp_stat)

    def run(self, model, host=None, port=None):
        """系统启动器"""
        self.model = model
        self.config()
        self.register()
        self.app.run(host, port)

    def manager(self):
        """app托管"""
        Migrate(self.app, db)
        manager = Manager(self.app)
        manager.add_command("db", MigrateCommand)
        return manager


apps = Application()
app = apps.app
