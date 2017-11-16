#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
"""
new_list = []
def split2len(obj):

    if len(obj) > 2:
        new_list = obj[0:2]
    else:
        new_list = obj
    return new_list


li = ['参数1', '参数2', '参数3']
opt = split2len(li)
print(opt)
