#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Power by HPCM 2019-05-27 10:14:49
# Filename load_setting.py
import os
import json

import yaml


# noinspection PyTypeChecker,PyUnresolvedReferences
class LoadSetting(object):
    def __init__(self, base_dir, model):
        self.base_dir = base_dir
        self.paths = {
            0: os.path.join("config", "location.yaml"),
            1: os.path.join("config", "product.yaml")
        }
        self.logging_path = os.path.join("config", "logging.json")
        self.model = int(model)
        self.conf = None

    def get_path(self):
        """获取路径"""
        if not isinstance(self.model, int):
            self.model = int(self.model)
        if self.model not in self.paths.keys():
            raise FileNotFoundError("配置文件不存在!, 请输入: {}".format(" ".join([str(i) for i in self.paths])))
        return os.path.join(self.base_dir, self.paths[self.model])

    def set_debug(self):
        """设置debug"""
        self.conf["debug"] = True if self.model == 0 else False

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
        conf_path = self.get_path()
        with open(conf_path, "r") as f:
            try:
                self.conf = yaml.load(f, Loader=yaml.FullLoader)
            except AttributeError:
                self.conf = yaml.load(f)
        self.set_other()
        return self.conf
