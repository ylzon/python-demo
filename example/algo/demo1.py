#!/usr/bin/env python
# -*- coding:utf-8 -*-


li = [11, 1, 1, 1, 1,  2, 35, 7, 34, 8, 1, 123, 23, 34, 511, 213, 34, 56, 0]


# 冒泡排序
def bubbling(arr):
    new_list = list(arr)

    for i in range(1, len(new_list)):
        for j in range(len(new_list) - i):

            if new_list[j] > new_list[j + 1]:
                temp = new_list[j]
                new_list[j] = new_list[j + 1]
                new_list[j + 1] = temp

    return new_list


new = bubbling(li)
print(new)
