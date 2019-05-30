#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Power by HPCM 2019-05-27 10:03:10
# Filename manager.py
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, "apps"))


def main():
    """获取app代理"""
    from application import apps
    apps.set_base_dir(BASE_DIR)
    apps.start()


if __name__ == "__main__":
    # noinspection PyBroadException
    try:
        sys.exit(main())
    except Exception:
        import traceback
        traceback.print_exc()
