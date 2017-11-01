#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 装饰器函数

import time


def decorator_2(func):
    """
    最外层装饰器
    :param func:
    :return:
    """
    def warp(*args, **kwargs):
        print("最外层装饰器".center(20, "="))
        ret = func(*args, **kwargs)
        print("最外层装饰器".center(20, "="))
        return ret

    return warp


def decorator_1(auth_type):
    """
    内层装饰器,计算函数运行时间
    :param auth_type:
    :return:
    """
    # print("auth type:", auth_type)

    def out_warp(func):
        # print("func:", func)

        def warp(*args, **kwargs):
            # print(*args, **kwargs)
            start_time = time.time()
            ret = func(*args, **kwargs)
            end_time = time.time()
            print("函数执行时间：", end_time - start_time)
            return ret

        return warp

    return out_warp


@decorator_2
@decorator_1(auth_type="local")
def main(*args, **kwargs):
    print("this is home,sleeping...")
    time.sleep(3)
    return args[0] + args[1]


i = main(1, 2)
print("最后返回结果:", i)
