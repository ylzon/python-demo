#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 题目三：
# 输出商品列表，用户输入序号，显示用户选中的商品
li = ["手机", "电脑", '鼠标垫', '游艇']

for index, text in enumerate(li, 1):
    print(index, text)

inp = input("请选择要购买的商品：")
inp_num = int(inp)
print(li[inp_num-1])