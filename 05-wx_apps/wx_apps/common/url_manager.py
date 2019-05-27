#!/usr/bin/env python
# encoding: utf-8
# author: HPCM
# time: 2019/5/27 22:43
# file: url_manager.py


def build_url(path):
    """基础管理"""
    return path


def build_static_url(path):
    """静态管理"""
    ver = 1.0
    path = "/static{}?ver={}".format(path, ver)
    return path
