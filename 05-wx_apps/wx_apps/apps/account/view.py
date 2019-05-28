# -*- coding:utf-8 -*-
# author:HPCM
# datetime:2019/5/28 9:44
from flask import Blueprint, render_template

bp_account = Blueprint("account", __name__, url_prefix="/account")


@bp_account.route("/index")
def index():
    return render_template("account/index.html")


@bp_account.route("/info")
def info():
    return render_template("account/info.html")


@bp_account.route("/set")
def set():
    return render_template("account/set.html")
