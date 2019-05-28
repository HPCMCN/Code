# -*- coding:utf-8 -*-
# author:HPCM
# datetime:2019/5/28 10:26
from flask import Blueprint, render_template

bp_stat = Blueprint("stat", __name__, url_prefix="/stat")


@bp_stat.route("/index")
def index():
    return render_template("stat/index.html")


@bp_stat.route("/food")
def food():
    return render_template("stat/food.html")


@bp_stat.route("/share")
def share():
    return render_template("stat/share.html")


@bp_stat.route("/vip")
def vip():
    return render_template("stat/vip.html")
