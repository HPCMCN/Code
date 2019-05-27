#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:hpcm
# datetime:19-5-27 下午4:21
from flask import Blueprint

bp_user = Blueprint("user", __name__, url_prefix="/user")


@bp_user.route("/test")
def test():
    from application import app
    return str(app.config.items())
