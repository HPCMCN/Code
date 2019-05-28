# -*- coding:utf-8 -*-
# author:HPCM
# datetime:2019/5/28 9:35
from flask import Blueprint, render_template

bp_index = Blueprint("index", __name__)


@bp_index.route("/index")
def index():
    return render_template("index/index.html")


@bp_index.route("/test")
def test():
    from common.url_manager import build_static_url, build_url
    path1 = build_url("/test")
    path2 = build_static_url("/test")
    msg = "<h1>path1: {}<br>path2:{}<h1>".format(path1, path2)
    return msg