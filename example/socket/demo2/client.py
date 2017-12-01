#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
客户端
"""

import socket
import os

sk = socket.socket()

addr = ("127.0.0.1", 9200)
file_path = "local/old.jpg"

# 建立连接
sk.connect(addr)

# 确认服务器返回信息
ret = str(sk.recv(1024), encoding="utf-8")
print(ret)

# 读取要上传文件大小
file_size = os.stat(file_path).st_size
sk.sendall(bytes(str(file_size), encoding="utf-8"))

# 接受服务端收到文件大小，防止粘包
sk.recv(1024)

# 发送文件
with open(file_path, "rb") as f:
    for line in f:
        sk.sendall(line)

# 关闭连接
sk.close()
