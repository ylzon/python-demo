#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 正则验证邮箱是否合法

import re


def is_email(addr):
    """
    判断是否是合法邮箱
    :param addr: 邮箱地址
    :return: True or False
    """
    re_is_email = re.compile("^[a-z0-9]+([._-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z]+$")
    if re_is_email.search(addr):
        return True
    else:
        return False


email = input("请输入订阅的邮箱地址：")
if is_email(email):
    print("订阅成功！")
else:
    print("订阅失败，您输入的邮箱不合法！")
