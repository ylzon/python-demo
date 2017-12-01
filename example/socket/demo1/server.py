#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
服务端
"""

import socket

sk = socket.socket()

# 绑定监听地址及IP
sk.bind(('127.0.0.1', 8888,))

# 监听最大数
sk.listen(5)

# 循环接受监听并输出客户端信息
print("[127.0.0.1:8888]已开启监听")
while True:
    conn, address = sk.accept()
    print(address, "|", conn)
