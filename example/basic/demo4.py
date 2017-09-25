#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 作业四：
#
# 要求用户输入总资产，例如：2000
# 显示商品列表，让用户根据序号选择商品，加入购物车
# 购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
# 附加：可充值、某商品移除购物车
import os

goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]
os.system("clear")
total = int(input("请输入您的总资产："))
cart = []  # 购物车
cart_sum = 0  # 总价格
cart_size = 0  # 总数量
while True:

    print "=======商品栏======="
    for i in range(0, len(goods)):
        print i + 1, goods[i].get('name')
    print "0 结束购物，查看购物车"
    print "==================="
    opt = int(input("请选择："))

    if opt == 0:
        while True:
            os.system("clear")
            print "=======购物车======="
            print "总资产：", total
            print "总价格：", cart_sum
            print "总数量：", cart_size
            for i in range(0, len(cart)):
                print i + 1, cart[i].get('name'), "价格", cart[i].get('price')
            print "9  [充值]"
            print "0  [结算]"
            print "删除商品请输入商品对应序号"
            print "==================="

            opt2 = int(input("请选择："))

            # 充值项
            if opt2 == 9:
                os.system("clear")
                top_up = int(input("请输入要充值的金额数："))
                total += top_up
                print "充值成功"
                continue

            # 结算项
            elif opt2 == 0:
                # !bug! macOS环境下，iTerm2终端下，Python2.7.11下该操作无效，PyCharm环境的命令行执行成功，该BUG尚未解决 2017年09月24日23:13:05 !bug!
                if cart_sum > total:
                    os.system("clear")
                    print "您的资产余额不足，还差", cart_sum - total, "请充值后重新结算"
                    continue
                else:
                    if cart_sum == 0:
                        os.system("clear")
                        print ("您尚未选购商品，请先选择商品并加入购物车！")
                        break
                    else:
                        os.system("clear")
                        print "已支付", cart_sum, "元，购买成功！"
                        total -= cart_sum
                        cart = []
                        cart_size = 0
                        cart_sum = 0
                        continue
            # 删除商品项
            else:
                if opt2 > cart_size:
                    os.system("clear")
                    print "指令输入有误，请重新选择！"
                    continue
                else:
                    os.system("clear")
                    print "已删除价格为[", cart[opt2 - 1].get('price'), "]的商品[", cart[opt2 - 1].get('name'), "]"
                    cart_size -= 1
                    cart_sum -= cart[opt2 - 1].get('price')
                    del cart[opt2 - 1]
                    continue

    # 添加商品到购物车
    else:
        if opt > len(goods):
            os.system("clear")
            print "指令输入有误，请重新选择！"
            continue
        else:
            os.system("clear")
            print "已添加价格为[", goods[opt - 1].get('price'), "]的商品[", goods[opt - 1].get('name'), "]到购物车"
            cart.append(goods[opt - 1])
            cart_size += 1
            cart_sum += goods[opt - 1].get('price')
