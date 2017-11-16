#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
"""


def is_odd(obj):
    new_list = []
    for i in range(0, len(obj)):
        if i % 2 != 0:
            new_list.append(obj[i])

    return new_list


li = ['参数0', '参数1', '参数2', '参数3']
opt = is_odd(li)
print(opt)
