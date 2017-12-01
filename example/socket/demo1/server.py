#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
服务端
"""

import socket

sk = socket.socket()

# 绑定监听地址及IP
sk.bind(('127.0.0.1', 6666,))

# 监听最大数
sk.listen(5)

# 循环接受监听并输出客户端信息
print("[127.0.0.1:8888]服务已开启监听")
while True:
    conn, address = sk.accept()
    # conn.sendall(bytes("欢迎进入机器人聊天系统", encoding="utf-8"))

    while True:
        ret_bytes = conn.recv(1024)
        ret_str = str(ret_bytes, encoding="utf-8")
        if ret_str == "q":
            break
        elif ret_str == "cd":
            conn.sendall(bytes("""
=======菜单=======
1.查询
2.激活
3.退订
4.预览
====回复序号选择====
            """, encoding="utf-8"))
        conn.sendall(bytes("[用户]" + ret_str, encoding="utf-8"))

