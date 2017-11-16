#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
利用第三方接口实现输入QQ号判断是否在线
"""

import requests
from xml.etree import ElementTree as ET


def is_online(qq_num):
    """
    调用第三方接口，查询qq号码是否在线
    :param qq_num: QQ号码，String
    :return: node.text String
    """
    data = requests.get("http://www.webxml.com.cn/webservices/qqOnlineWebService.asmx/qqCheckOnline?qqcode=%s" % qq_num)
    result = data.text
    node = ET.XML(result)

    return node.text


def main():
    """
    主函数
    :return: None
    """
    inp = input("请输入要查询的QQ号：")
    result = is_online(inp)
    if result == "Y":
        print("[%s]在线" % inp)
    elif result == "N":
        print("[%s]离线" % inp)
    elif result == "E":
        print("QQ号码错误！")
    else:
        print("您输入的内容有误！")


if __name__ == '__main__':
    main()
