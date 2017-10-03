#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 写函数，检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有空内容。

def is_None(obj):
    index = 1
    isN = False
    for i in obj:
        if i == None or i.isspace() == True or i == '':
            isN = True
        index += 1
    if isN:
        print(obj, '有空内容')
    else:
        print(obj, '无空内容')


obj1 = 'asd324sdfsd'
obj2 = ['k1', '']
obj3 = ('a', 'b', '')

is_None(obj1)
is_None(obj2)
is_None(obj3)
