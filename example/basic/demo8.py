#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数

def isStr(s):
    num_count = 0
    alp_count = 0
    spc_count = 0
    oth_count = 0
    for i in s:
        if i.isnumeric() == True:
            num_count += 1
            continue
        elif i.isalpha() == True:
            alp_count += 1
            continue
        elif i.isspace() == True:
            spc_count += 1
            continue
        else:
            oth_count += 1
            continue
    info = """数字:{}
字母:{}
空格:{} 
其他:{}"""
    print(info.format(num_count, alp_count, spc_count, oth_count))


isStr('asdasd 1 23as dvds ,asd*,123123')
