#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:hpcm
# datetime:19-5-27 下午4:21
from flask import Blueprint, render_template, request, jsonify

from config import constants
from common.model import User

bp_user = Blueprint("user", __name__, url_prefix="/user")


@bp_user.route("/login", methods=["GET", "POST"])
def user():
    method = request.method.upper()
    if method == "GET":
        return render_template("user/login.html")
    elif method == "POST":
        username = request.form.get("login_name", None)
        password = request.form.get("login_pwd", None)
        validates = (
            (username, 14001),
            (password, 14002)
        )
        for k, v in filter(lambda x: not x[0], validates):
            return jsonify(constants.msg(v))
        u = User.query.filter_by(username=username).all()
        if not u:
            return jsonify(constants.msg(14003))
        if u[0].check_password(password) is False:
            return jsonify(constants.msg(14004))
        return jsonify(constants.msg(12001))


@bp_user.route("/edit")
def edit():
    return render_template("user/edit.html")


@bp_user.route("/reset-pwd")
def reset_pwd():
    return render_template("user/reset_pwd.html")
