#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
客户端
"""

import socket

sk = socket.socket()

# 建立访问
sk.connect(("127.0.0.1", 8888,))

# 结束访问
print("访问成功")
sk.close()
