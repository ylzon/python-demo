#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
# 实现用户登录、注册操作，并以文本文件保存用户名密码数据
"""

def login(username, password):
    """
    作用：用户名密码验证
    :param username: 用户名
    :param password: 密码
    :return: True or False 判断用户是否登录成功
    """

    with open("db", "r", encoding="utf-8") as f:
        for line in f:
            info = line.strip().split("@")

            # 判断用户名密码是否都正确
            if username == info[0] and password == info[1]:
                return True

        else:
            # 判断用户名密码不正确返回False
            return False


def register(username, password):
    """
    用户注册模块
    :param username: 用户名
    :param password: 密码
    :return: True or False 注册成功与否
    """
    with open("db", "a+", encoding="utf-8") as f:

        # 判断是否存在该用户，如不存在直接存入db文件
        if not user_exist(username):
            f.write("\n" + username + "@" + password)
            return True
        else:
            return False


def user_exist(username):
    """
    判断用户是否存在
    :param username: 用户名
    :return: True or False 用户是否存在
    """

    with open("db", "r", encoding="utf-8") as f:
        for line in f:
            result = line.strip().split("@")

            # 判断是否是存在该用户
            if username == result[0]:
                return True
        else:
            # 不存在则返回False
            return False


def main():
    # 选择登录or注册
    print("1.登录\n2.注册")
    inp = input("请输入对应的数字选择：")

    # 用户登录
    if inp == "1":
        user = input("请输入账户：")
        pwd = input("请输入密码：")
        if login(user, pwd):
            print("登录成功")
        else:
            print("登录失败，用户名或密码错误！")

    # 用户注册
    elif inp == "2":
        reg_user = input("请输入要添加的账户：")
        reg_pwd = input("请输入要添加的密码：")
        if register(reg_user, reg_pwd):
            print("注册成功")
        else:
            print("注册失败，该用户已存在！")

    # 输入有误
    else:
        print("输入错误！")


main()
