#!/usr/bin/env python
# -*- coding:utf-8 -*-

old_dict = {
    "#1": 11,
    "#2": 22,
    "#3": 33
}

new_dict = {
    "#1": 11,
    "#3": 44,
    "#4": 100
}

info = '''

需要删除：{1}
需要新建：{2}
需要更新：{3}
'''

old_set = set(old_dict.keys())
new_set = set(new_dict.keys())

# 在old中，删除old中存在，new中不存在的
del_set = old_set.difference(new_set)

# 在old中，新建new中存在，old中不存在的
add_set = new_set.difference(old_set)

# 在old中，更新两个中都存在的
rep_set = old_set.intersection(new_set)

print(info.format(del_set, add_set, rep_set))
