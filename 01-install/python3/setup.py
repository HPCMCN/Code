#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:hpcm
# datetime:19-4-24 下午8:47
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# 将项目添加到环境中
from install import app


class PythonInstaller(app.Installer):
    """Linux python 安装"""

    def __init__(self):
        self.base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "libs")
        super().__init__()

    @app.route("gcc", "gcc --version")
    def install_gcc(self, path):
        """安装gcc"""
        os.chdir(path)
        i = os.system("bash ./install_gcc.sh")
        return i == 0

    @app.route("ssl_devel", "openssl version -a")
    def install_openssl(self, path):
        """安装openssl"""
        os.chdir(path)
        i = os.system("rpm -Uvh *.rpm --nodeps --force") or \
            os.system(
                "echo 'export LD_LIBRARY_PATH=/usr/lib64:/usr/lib:/usr/local/lib:/usr/local/lib64:$LD_LIBRARY_PATH'")
        return i == 0

    @app.route("zlib", "cat $(path=`find /usr/ -name zlib.pc`;if [ \"$path\" == "" ];then echo 1; else echo $path;fi)")
    def install_zlib(self, path):
        """安装zlib"""
        os.chdir(path)
        i = os.system("./configure") or \
            os.system("make") or \
            os.system("make install")
        return i == 0

    @app.route("python", "python3 --version")
    def install_python(self, path):
        """安装python"""
        os.chdir(path)
        i = os.system("./configure  --prefix=/usr/local/python3 --enable-shared") or \
            os.system("make -j4") or \
            os.system("make install") or \
            os.system("cp libpython3.5m.so.1.0 /usr/local/lib64/") or \
            os.system("cp libpython3.5m.so.1.0 /usr/lib/") or \
            os.system("cp libpython3.5m.so.1.0 /usr/lib64/") or \
            os.system("echo 'export PATH=$PATH:/usr/local/python3/bin' >> /root/.bashrc") or \
            any(os.system(
                "echo 'export PATH=$PATH:/usr/local/python3/bin' >> {}/.bashrc".format(os.path.join("/home", path))) for
                path in os.listdir("/home"))
        return i == 0


if __name__ == "__main__":
    pi = PythonInstaller()
    pi.run()
