# -*- coding:utf-8 -*-
# author:HPCM
# datetime:2019/5/29 16:50
def f1(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper



