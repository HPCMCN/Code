#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Power by HPCM 2019-05-27 10:03:10
# Filename manager.py
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, "apps"))


def get_manager():
    """获取app代理"""
    from application import apps
    apps.base_dir = BASE_DIR
    manage = apps.manager()

    @manage.option("-m", "--model", help="运行的模式: 1. 生产模式 2. 测试模式", dest="model", default=1)
    @manage.option("-h", "--host", help="服务运行的ip及端口", dest="host", default="0.0.0.0:5000")
    def run(model, host):
        """命令行运行函数"""
        try:
            host, port = host.split(":")
        except ValueError:
            raise TypeError("ip与端口输入方式必须为ip:port!")
        apps.run(model, host=host, port=int(port))
    return manage


if __name__ == "__main__":
    try:
        sys.exit(get_manager().run())
    except Exception as e:
        import logging
        logging.getLogger("wx")
        logging.info(e)
