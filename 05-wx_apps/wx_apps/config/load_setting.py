#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Power by HPCM 2019-05-27 10:14:49
# Filename load_setting.py
import os
import logging.config

import yaml

import logging.config

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(levelname).4s %(asctime)s] %(module)s %(lineno)d %(message)s'
        },
        'simple': {
            'format': '[%(levelname).4s %(asctime)s] %(module)s %(lineno)d %(message)s'
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                "stream": "ext://sys.stdout",
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
            'file': {
                'level': 'INFO',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': "logs/running.log",  # 日志文件的位置
                'maxBytes': 300 * 1024 * 1024,
                'backupCount': 10,
                'formatter': 'verbose'
            },
        },
        'loggers': {
            'wx': {
                "level": "INFO",
                'handlers': ['console', 'file'],
                'propagate': True,
            },
        }
    }
}

logging.config.dictConfig(LOGGING)


class LoadSetting(object):
    def __init__(self, base_dir, model):
        self.base_dir = base_dir
        self.paths = {
            0: "config/location.yaml",
            1: "config/product.yaml"
        }
        self.model = int(model)

    def get_path(self):
        """获取路径"""
        if not isinstance(self.model, int):
            self.model = int(self.model)
        if self.model not in self.paths.keys():
            raise FileNotFoundError("配置文件不存在!, 请输入: {}".format(" ".join([str(i) for i in self.paths])))
        return os.path.join(self.base_dir, self.paths[self.model])

    @property
    def cfg(self):
        """启动器"""
        conf_path = self.get_path()
        with open(conf_path, "r") as f:
            try:
                conf = yaml.load(f, Loader=yaml.FullLoader)
            except AttributeError:
                conf = yaml.load(f)
            conf["debug"] = True if self.model == 0 else False
        return conf
