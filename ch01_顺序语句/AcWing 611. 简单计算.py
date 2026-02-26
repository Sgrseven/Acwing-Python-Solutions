# -*- coding: utf-8 -*-
"""
@File    : AcWing 611. 简单计算.py
@Author  : Sgrseven
@Date    : 2026/2/25 20:45
@Link    : https://www.acwing.com/problem/content/613/
"""

"""
题解思路：
1. 利用 map(str.split, stdin) 获取全部输入，并逐行按空格切分为列表。
2. 遍历每行数据 x，忽略编号 x[0]，直接取数量 x[1] 和单价 x[2] 相乘。
3. 通过 sum() 将所有产品的总价进行累加。
4. 使用 f-string 的 :.2f 将总金额固定保留两位小数输出。
"""
from sys import stdin
print(f'VALOR A PAGAR: R$ {sum(int(x[1]) * float(x[2]) for x in map(str.split, stdin)):.2f}')
