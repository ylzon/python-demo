# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
文件服务器
"""

import socket

sk = socket.socket()

addr = ("127.0.0.1", 9200)
upload_path = "upload/new.jpg"

sk.bind(addr)
sk.listen(5)

while True:
    conn, address = sk.accept()
    conn.sendall(bytes("连接成功", encoding="utf-8"))

    # 接受要上传文件的大小
    file_size = int(str(conn.recv(1024), encoding="utf-8"))
    print("用户要上传的文件大小:", file_size)

    # 已接收客户端发来的文件大小，返回确认信息，防止粘包
    conn.sendall(bytes("AYC", encoding="utf-8"))

    # 已接受文件大小
    has_size = 0

    # 接受文件并存入upload文件夹
    f = open(upload_path, "wb")
    while True:

        # 文件上传完成跳出
        if has_size == file_size:
            break
        data = conn.recv(1024)
        f.write(data)

        has_size += len(data)

    # 关闭文件
    print("文件上传完毕")
    f.close()
