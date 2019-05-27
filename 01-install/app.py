#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:hpcm
# datetime:19-4-26 下午3:30
import os
import shutil
import functools
import collections

route_map = collections.OrderedDict()


# install_app_name: [install_func, app_path]

class InstallerMeta(type):
    """创建元类, 保证子类运行必须提供当前文件位置"""

    def __call__(cls, *args, **kwargs):
        obj = super().__call__(*args, **kwargs)
        for name in filter(lambda x: not hasattr(obj, x), ["base_path"]):
            raise AttributeError("{} attribute is not set!".format(name))
        return obj


# noinspection PyUnresolvedReferences
class Installer(metaclass=InstallerMeta):
    """安装基类"""

    def __init__(self):
        self.route_map = route_map
        self.zip_type = {
            ".zip": "zip",
            ".tar": "tar",
            ".gz": "gztar",
            ".tgz": "gztar",
            ".bz": "bztar",
            ".xz": "xztar"
        }

    def unzip_lib(self):
        """解压libs中的压缩包"""
        history_file = os.listdir(self.base_path)
        for path, name in map(lambda x: (os.path.join(self.base_path, x), x), history_file):
            # 迭代文件下全部文件---> 绝对路径, 相对路径
            if os.path.isfile(path):
                for key in filter(lambda x: name.lower().startswith(x), self.route_map.keys()):
                    # 如果是文件, 则进行检查, 是否为解压文件---> 待安装的程序名称
                    shutil.unpack_archive(path, self.base_path, self.zip_type[os.path.splitext(path)[1]])
                    for name_path in filter(
                            lambda x: x.lower().startswith(key) and os.path.isdir(os.path.join(self.base_path, x)),
                            os.listdir(self.base_path)):
                        # 检查解压文件是否存在 --> 解压后的文件名(绝对路径)
                        print(name_path)
                        if len(self.route_map[key]) < 2:
                            self.route_map[key].append(os.path.join(self.base_path, name_path))
                            break
                        else:
                            raise ValueError("Route map values max length can't greater than 2!")
                    else:
                        raise shutil.ExecError("Unpack archive {} failed!".format(key))

    def install(self):
        """安装路由中全部libs"""
        for e in filter(lambda x: len(x[1]) != 2, self.route_map.items()):
            raise ValueError("{} is not unpack file".format(e[0]))
        for key, value in self.route_map.items():
            if getattr(self, value[0])(value[1]) is not True:
                print("[INFO] {} install failed!".format(key))
                break
            else:
                print("[INFO] {} install success!".format(key))

    def run(self):
        self.unzip_lib()
        self.install()


def route(name, cmd=None):
    """路由装饰"""

    def inner_func(func):
        if cmd is not None and os.system(cmd) == 0:
            return True
        route_map[name] = [func.__name__]

        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            if cmd is not None:
                return func(self, *args, **kwargs) and os.system(cmd) == 0
            else:
                return func(self, *args, **kwargs)

        return wrapper

    return inner_func


if __name__ == "__main__":
    class Test(Installer):
        def __init__(self):
            super().__init__()


    Test()
