#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
简述普通参数、指定参数、默认参数、动态参数的区别?
"""

# 1普通参数
def general(s):
    print('普通参数：', s)


general("参数1")


# 2指定参数
def spec(a, b):
    print('指定参数：', a, b)


spec(b="参数1", a="参数2")


# 3默认参数
def default(s="默认参数"):
    print('默认参数：', s)


default()


# 4动态参数1-元祖形式
def dynamic1(*args):
    print('动态参数-元祖形式：', args)


# 方式一：dynamic1('参数1', '参数2')
# 方式二：
args = ['参数1', '参数2']
dynamic1(*args)


# 5动态参数2-字典形式
def dynamic2(**kwargs):
    print('动态参数-字典形式：', kwargs)


# 方式一：
# dynamic2(k1="参数1", k2="参数2")

# 方式二：
kw = {'k1': '参数1', 'k2': '参数2'}
dynamic2(**kw)
