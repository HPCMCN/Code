#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Power by HPCM 2019-05-27 10:13:04
# Filename constants.py
import os
import sys

DEBUG = True


class Config(object):
    """配置文件导入"""
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(BASE_DIR)
    sys.path.append(os.path.join(BASE_DIR, "apps"))

    def __init__(self):
        from config.load_setting import LoadSetting
        cfg = LoadSetting(Config.BASE_DIR, DEBUG).cfg
        for k, v in cfg.items():
            setattr(self, k.upper(), v)
