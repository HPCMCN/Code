#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:hpcm
# datetime:19-5-27 下午4:21
from flask import Blueprint, render_template

bp_user = Blueprint("user", __name__, url_prefix="/user")


@bp_user.route("/login")
def user():
    return render_template("/user/login.html")


@bp_user.route("/test")
def test():
    from common.url_manager import build_static_url, build_url
    path1 = build_url("/test")
    path2 = build_static_url("/test")
    msg = "<h1>path1: {}<br>path2:{}<h1>".format(path1, path2)
    return msg
