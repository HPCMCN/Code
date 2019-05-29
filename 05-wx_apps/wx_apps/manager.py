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
    manager = apps.manager

    @manager.option("-h", "--host", help="服务运行的ip及端口", dest="host", default="0.0.0.0:5000")
    def run(host):
        """命令行运行函数"""
        try:
            host, port = host.split(":")
        except ValueError:
            raise TypeError("ip与端口输入方式必须为ip:port!")
        apps.run(host=host, port=int(port))
    return manager


if __name__ == "__main__":
    # noinspection PyBroadException
    try:
        sys.exit(get_manager().run())
    except Exception:
        import traceback
        traceback.print_exc()
