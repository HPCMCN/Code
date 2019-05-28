# -*- coding:utf-8 -*-
# author:HPCM
# datetime:2019/5/28 10:09
from flask import Blueprint, render_template

bp_food = Blueprint("food", __name__, url_prefix="/food")


@bp_food.route("cat")
def cat():
    return render_template("food/cat.html")


@bp_food.route("cat-set")
def cat_set():
    return render_template("food/cat_set.html")


@bp_food.route("index")
def index():
    return render_template("food/index.html")


@bp_food.route("info")
def info():
    return render_template("food/info.html")


@bp_food.route("set")
def set_():
    return render_template("food/set.html")
