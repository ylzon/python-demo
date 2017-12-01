#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
客户端
"""

import socket

sk = socket.socket()

# 建立访问
sk.connect(("127.0.0.1", 6666,))

# 结束访问


while True:
    message = input("请输入要发送的消息(输入q退出,cd进入菜单)：")
    if message == "q":
        sk.sendall(bytes(message, encoding="utf-8"))
        break
    else:
        sk.sendall(bytes(message, encoding="utf-8"))
        ret = str(sk.recv(1024), encoding="utf-8")
        print(ret)

sk.close()
