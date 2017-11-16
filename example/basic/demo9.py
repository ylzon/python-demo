#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
"""

def is_length(obj):
    obj_len = 0
    for i in obj:
        obj_len += 1
    if obj_len > 5:
        print(obj, "长度大于5")
    else:
        print(obj, "长度为", obj_len)


obj1 = 'asd324sdfsd'
obj2 = ['k1', 'k2']
obj3 = ('a', 'b', 'c')

is_length(obj1)
is_length(obj2)
is_length(obj3)
