#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
配置文件的增删改查
"""

import configparser

conf = configparser.ConfigParser()
conf.read(".config", encoding="utf-8")

# 获取所有的节点
v1 = conf.sections()
print(v1)

# 获取指定节点下的所有键
v2 = conf.options("Setting")
print(v2)

# 获取指定节点下所有的键值对
v3 = conf.items("Setting")
print(v3)

# 获取指定节点、指定键对应的值
v4 = conf.get("Setting", "year")
print(v4)

# 检查节点是否存在
has_node = conf.has_section("Setting")
print(has_node)

# 检查指定节点下的键值对是否存在
has_attr = conf.has_option("Setting", "year")
print(has_attr)

# 删除键值对
conf.remove_option("Attr", "test")
conf.write(open(".config", "w"))

# 删除节点
conf.remove_section("Attr")
conf.write(open(".config", "w"))

# 添加节点
conf.add_section("Attr")
conf.write(open(".config", "w"))

# 添加键值对
conf.set("Attr", "test", "name")
conf.write(open(".config", "w"))



