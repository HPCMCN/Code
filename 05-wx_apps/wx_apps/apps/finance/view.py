# -*- coding:utf-8 -*-
# author:HPCM
# datetime:2019/5/28 10:19
from flask import Blueprint, render_template

bp_finance = Blueprint("finance", __name__, url_prefix="/finance")


@bp_finance.route("/index")
def index():
    return render_template("finance/index.html")


@bp_finance.route("/account")
def account():
    return render_template("finance/account.html")


@bp_finance.route("/pay-info")
def pay_info():
    return render_template("finance/pay_info.html")
