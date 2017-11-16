#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
随机产生验证码
"""

import random

code = ""
for i in range(4):

    num = random.randrange(0, 2)

    # 当前位显示字母或者数字各有50%几率
    if num == 0:
        # 随机显示数字
        r1 = random.randrange(0, 10)
        code += str(r1)
    else:
        # 随机显示字母
        i = random.randrange(65, 91)
        c = chr(i)
        code += c

print(code)
