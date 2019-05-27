#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:hpcm
# datetime:19-4-29 下午3:31
import rpyc

s_obj = rpyc.connect("localhost", 22222)
print(s_obj.root.now_time())
print(s_obj.root.new())
s_obj.close()
