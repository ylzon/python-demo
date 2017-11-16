#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
1. 写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
2. 字典中的value只能是字符串或列表
"""
dic = {
    "k1": "v1v1",
    "k2": [
        11,
        22,
        33,
        44
    ]
}


def is_len2(obj):
    new_list = {}
    for i in obj:
        new_list[i] = obj[i][0:2]

    return new_list


opt = is_len2(dic)
print(opt)
