#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:hpcm
# datetime:19-4-28 下午3:56
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

    @app.route("gcc")
    def install_gcc(self, path):
        """安装gcc"""
        os.chdir(path)
        i = os.system("rpm -Uvh  *.rpm  --nodeps  --force")
        return i == 0

    @app.route("pcre", "tail -n 10 \"$(rpm -qa pcre)\"")
    def install_pcre(self, path):
        """安装pcre"""
        os.chdir(path)
        i = os.system("./configure --disable-shared --with-pic") or \
            os.system("make") or \
            os.system("make install")
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

    @app.route("nginx", "nginx -v")
    def install_nginx(self, path):
        """安装nginx"""
        os.chdir(path)
        i = os.system(
            "./configure --prefix=../server --with-http_ssl_module \
            --with-pcre=../pcre-8.42 \
            --with-zlib=../zlib-1.2.11") or \
            os.system("make") or \
            os.system("make install")
        return i == 0


if __name__ == "__main__":
    pi = PythonInstaller()
    pi.run()
