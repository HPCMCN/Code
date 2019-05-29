# -*- coding:utf-8 -*-
# author:HPCM
# datetime:2019/5/28 14:16
from flask import Blueprint, render_template, abort

bp_error = Blueprint("error", __name__, url_prefix="/error")


@bp_error.errorhandler(BaseException)
def error_4(e):
    print(e)
    return render_template("error/error.html"), 404


@bp_error.route("/test")
def error():
    abort(404)
    return ""


@bp_error.after_request
def get_400(request):
    print(request)
    return request


@bp_error.after_request
def get_error(e):
    print(e)
