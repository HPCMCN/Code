#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:hpcm
# datetime:19-4-24 下午3:53
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# 将项目添加到环境中
from install import app


class RedisInstaller(app.Installer):
    """Linux python 安装"""

    def __init__(self):
        self.base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "libs")
        super().__init__()

    @app.route("tcl")
    def install_gcc(self, path):
        """安装tcl"""
        os.chdir(os.path.join(path, "unix"))
        if os.system("echo 'puts $tcl_version;exit 0' | tclsh") == 0:
            return True
        i = os.system("./configure") or \
            os.system("make") or \
            os.system("make install") or \
            os.system("echo 'puts $tcl_version;exit 0' | tclsh")
        return i == 0

    @app.route("redis")
    def install_openssl(self, path):
        """安装openssl"""
        os.chdir(path)
        if os.system("redis-server --version") == 0:
            return True
        i = os.system("make") or \
            os.system("taskset -c 0 make test") or \
            os.system("make PREFIX=/usr/local/redis install") or \
            os.system("redis-server --version")
        # 如果机器性能不好可能会导致test不通过, 可以直接跳过安装
        return i == 0


if __name__ == "__main__":
    ri = RedisInstaller()
    ri.run()
