#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
服务端
"""

import socket
import select

# 创建socket
sk = socket.socket()
sk.bind(("127.0.0.1", 8989))
sk.listen(10)

# 初始化参数
inputs = [sk, ]  # 存放输入的conn及wk对象
outputs = []  # 存放输出内容的conn
message_dict = {}  # 存放客户端发送到信息和conn
inte_time = 1

while True:
    # 利用select构建IO多路复用
    r_list, w_list, e_list = select.select(inputs, outputs, inputs, inte_time)

    print("当前在线人数[%s]:%s" % (len(inputs) - 1, r_list))

    # 读取连接客户端，并加入r_list监听
    for sk_or_conn in r_list:

        # 如果是sk服务器对象，则代表有新用户连接
        if sk_or_conn == sk:

            # 将新用户的连接对象加入select监听
            conn, addr = sk_or_conn.accept()
            inputs.append(conn)
            message_dict[conn] = []

        # 表示已连接用户已发送消息
        else:
            # 防止客户端传空字符串报错使程序崩溃
            try:
                # 获取客户端发送的数据
                acc_data_bytes = sk_or_conn.recv(1024)
            except Exception as ex:
                # 显示报错信息，并将出错的客户端连接从inputs中移除
                print(ex)
                inputs.remove(sk_or_conn)
            else:
                # 正常接受用户发送的消息，并存入消息字典
                acc_data_str = str(acc_data_bytes, encoding="utf-8")
                message_dict[sk_or_conn].append(acc_data_str)

                # 将发过消息的用户放入outputs，便于回复
                outputs.append(sk_or_conn)

    # 自动回复发送消息的客户端
    for conn in w_list:
        # 获取到客户端发送的数据，放入内存并删除
        recv_data = message_dict[conn][0]
        del message_dict[conn][0]
        conn.sendall(bytes("您说：" + recv_data, encoding="utf-8"))
        outputs.remove(conn)

    # 自动移除多socket中出错的对象
    for sk in e_list:
        inputs.remove(sk)
