#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:hpcm
# datetime:19-5-27 下午4:21
from flask import Blueprint, render_template

bp_user = Blueprint("user", __name__, url_prefix="/user")


@bp_user.route("/login")
def user():
    return render_template("/user/login.html")


@bp_user.route("/edit")
def edit():
    return render_template("/user/edit.html")


@bp_user.route("/reset-pwd")
def reset_pwd():
    return render_template("user/reset_pwd.html")





