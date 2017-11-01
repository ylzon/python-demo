#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 利用生成器实现并行效果

import time


def consumer(name):
    print("%s进入包子店" % name)
    while True:
        baozi = yield
        print("第[%s]笼包子来了，被[%s]吃了" % (baozi, name))


def producer():
    c1 = consumer("顾客A")
    c2 = consumer("顾客B")

    c1.__next__()
    c2.__next__()

    for i in range(1, 11):
        time.sleep(3)
        print("厨师做了第%d笼包子".center(20, "=") % i)
        c1.send(i)
        c2.send(i)


producer()
