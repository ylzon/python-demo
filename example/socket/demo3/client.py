#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
客户端
"""

import socket

sk = socket.socket()
sk.connect(("127.0.0.1", 8989))

while True:
    inps = input("请输入要发送的内容：")
    sk.sendall(bytes(inps, encoding="utf-8"))
    acc_data = str(sk.recv(1024), encoding="utf-8")
    print(acc_data)
