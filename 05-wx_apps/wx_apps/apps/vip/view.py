# -*- coding:utf-8 -*-
# author:HPCM
# datetime:2019/5/28 9:59
from flask import Blueprint, render_template

bp_vip = Blueprint("vip", __name__, url_prefix="/vip")


@bp_vip.route("/index")
def index():
    return render_template("vip/index.html")


@bp_vip.route("/comment")
def comment():
    return render_template("vip/comment.html")


@bp_vip.route("/info")
def info():
    return render_template("vip/info.html")


@bp_vip.route("/set")
def set_():
    return render_template("vip/set.html")
