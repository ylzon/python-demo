#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 利用递归计算斐波那契数列
def recu(a1, a2, arr):
    """
    计算斐波那契数列
    :param a1: 第一个值
    :param a2: 第二个值
    :param arr: 保存斐波那契数列的数组
    :return: 大于100000则返回False
    """
    if a1 > 100000:
        return False
    arr.append(a1)
    a3 = a1 + a2
    recu(a2, a3, arr)


def main():
    fib = []
    recu(0, 1, fib)
    print("斐波那契序列：", fib)


main()
