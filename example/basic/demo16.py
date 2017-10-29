#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 装饰器

def outer(func):
    def inner(*args, **kwargs):
        print("开始")
        ret = func(*args, **kwargs)
        print("结束")
        return ret

    return inner


@outer
def main(a1, a2):
    print("内容")
    return a1 + a2


ret = main(1, 2)
print(ret)
