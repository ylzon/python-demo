# Basic 基础练习

## Demo-1

* 有如下值集合 [11,22,33,44,55,66,77,88,99,90]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。
* 即： {'k1': 大于66的所有值, 'k2': 小于66的所有值}

 参考Demo：[链接](https://github.com/mgss/python-demo/blob/master/example/basic/demo1.py)

## Demo-2

* 查找列表中元素，移除每个元素的空格，并查找以 a或A开头 并且以 c 结尾的所有元素。

```python
li = ["alec", " aric", "Alex", "Tony", "rain"]
tu = ("alec", "aric", "Alex", "Tony", "rain")
dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}
```

 参考Demo：[链接](https://github.com/mgss/python-demo/blob/master/example/basic/demo2.py)


## Demo-3

* 输出商品列表，用户输入序号，显示用户选中的商品

```python
li = ["手机", "电脑", '鼠标垫', '游艇']
```

 参考Demo：[链接](https://github.com/mgss/python-demo/blob/master/example/basic/demo3.py)


## Demo-4

* 要求用户输入总资产，例如：2000
* 显示商品列表，让用户根据序号选择商品，加入购物车
* 购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
* 附加：可充值、某商品移除购物车

```python
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]
```

 参考Demo：[链接](https://github.com/mgss/python-demo/blob/master/example/basic/demo4.py)


## Demo-5

* 用户交互，显示省市县三级联动的选择

```python
dic = {
    "河北": {
        "石家庄": ["鹿泉", "藁城", "元氏"],
        "邯郸": ["永年", "涉县", "磁县"],
    },
    "河南": {
        "石家庄2": ["鹿泉2", "藁城2", "元氏2"],
        "邯郸2": ["永年2", "涉县2", "磁县2"],
    },
    "山西": {
        "石家庄3": ["鹿泉3", "藁城3", "元氏3"],
        "邯郸3": ["永年3", "涉县3", "磁县3"],
    }
}
```

 参考Demo：[链接](https://github.com/mgss/python-demo/blob/master/example/basic/demo5.py)

 ## Demo-6

* 在old中，删除old中存在，new中不存在的
* 在old中，新建new中存在，old中不存在的
* 在old中，更新两个中都存在的

```python
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
```

 参考Demo：[链接](https://github.com/mgss/python-demo/blob/master/example/basic/demo6.py)