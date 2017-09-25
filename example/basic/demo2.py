#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 题目二：
# 查找列表中元素，移除每个元素的空格，并查找以 a或A开头 并且以 c 结尾的所有元素。

li = ["alec", " aric", "Alex", "Tony", "rain"]
tu = ("alec", " aric", "Alex", "Tony", "rain")
dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}

tump = []

for i in range(0, len(li)):
    # 去除元素空格
    li[i] = li[i].strip()
    # 以a或A开头,且以c结尾的所有元素
    if li[i].endswith('c') and li[i].capitalize().startswith('A'):
        tump.append(li[i])

for i in range(0, len(tu)):
    # 以a或A开头,且以c结尾的所有元素
    if tu[i].endswith('c') and tu[i].capitalize().startswith('A'):
        tump.append(tu[i])

for item in dic.values():
    # 去除元素空格
    item = item.strip()
    # 以a或A开头,且以c结尾的所有元素
    if item.endswith('c') and item.capitalize().startswith('A'):
        tump.append(item)

for i in range(0, len(tump)):
    tump[i].strip()

txt = "以a或A开头,且以c结尾的所有元素"
print("list:",li)
print("tuple:",tu)
print("dict:",dic)
print(txt.center(50, "="))
print(tump)
