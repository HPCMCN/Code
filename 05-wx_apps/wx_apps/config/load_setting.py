#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Power by HPCM 2019-05-27 10:14:49
# Filename load_setting.py
import os

import yaml


# noinspection PyTypeChecker,PyUnresolvedReferences
class LoadSetting(object):
    """获取配置"""

    def __init__(self, base_dir, debug):
        self.base_dir = base_dir
        self.debug = debug
        self.conf_path = os.path.join("config", "location.yaml") if self.debug is True else os.path.join(
            "config", "product.yaml")
        self.logging_path = os.path.join("config", "logging.json")
        self.massage_path = os.path.join("config", "massage.yaml")
        self.conf = None

    def set_debug(self):
        """设置debug"""
        self.conf["debug"] = self.debug

    def set_log(self):
        """设置日志"""
        import json
        with open(os.path.join(self.base_dir, self.logging_path), "r") as f:
            log = json.load(f)
        temp = log["handlers"]["file"]["filename"]
        out_path = self.base_dir
        r_t = temp.split("/")
        if len(r_t) == 1:
            r_t = temp.split("\\")
        for path in r_t:
            out_path = os.path.join(out_path, path)
        log["handlers"]["file"]["filename"] = out_path
        self.conf["LOGGER"] = log

    def set_other(self):
        """设置其他的项目"""
        self.set_debug()
        self.set_log()

    @property
    def cfg(self):
        """启动器"""
        with open(self.conf_path, "r") as f:
            try:
                self.conf = yaml.load(f, Loader=yaml.FullLoader)
            except AttributeError:
                self.conf = yaml.load(f)
        self.set_other()
        return self.conf

    def set_massage(self):
        """启动器"""
        with open(self.massage_path, "r") as f:
            try:
                msg = yaml.load(f, Loader=yaml.FullLoader)
            except AttributeError:
                msg = yaml.load(f)
        return msg
