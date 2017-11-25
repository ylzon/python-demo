#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
基于反射实现简单路由模块函数功能
"""

inp = input("请输入要执行的模块函数（例如：demo20/main）：")

target_module, target_func = inp.split("/")

m = __import__(target_module)

if hasattr(m, target_func):
    print("接下来是%s的运行结果" % inp)
    func = getattr(m, target_func)
    func()

else:
    print("404")


