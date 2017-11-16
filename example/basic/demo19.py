#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
实现命令行进度条，带百分比
"""

import sys
import time

for i in range(101):
    # 清除屏幕
    sys.stdout.write("\r")

    # 显示百分比和进度条
    sys.stdout.write("[%s%%|%-100s]" % (i, i * ('█')))

    # 从缓存刷入到屏幕
    sys.stdout.flush()

    # 延时0.3秒
    time.sleep(0.3)
