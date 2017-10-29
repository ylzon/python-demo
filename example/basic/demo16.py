#!/usr/bin/env python
# -*- coding:utf-8 -*-



# 多层装饰器
def outer_fist(func):
    def inner(*args, **kwargs):
        print("第一层开始")
        ret = func(*args, **kwargs)
        print("第一层结束")
        return ret

    return inner


def outer(func):
    def inner(*args, **kwargs):
        print("开始")
        ret = func(*args, **kwargs)
        print("结束")
        return ret

    return inner


@outer_fist
@outer
def main(a1, a2):
    print("内容")
    return a1 + a2


ret = main(1, 2)
print(ret)
