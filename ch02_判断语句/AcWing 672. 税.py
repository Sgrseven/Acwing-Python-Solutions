# -*- coding: utf-8 -*-
"""
@File    : AcWing 672. 税.py
@Author  : Sgrseven
@Date    : 2026/3/7 23:44
@Link    : https://www.acwing.com/problem/content/674/
"""

s = float(input())

if s <= 2000:
    print("Isento")
elif s <= 3000:
    print(f"R$ {(s - 2000) * 0.08:.2f}")
elif s <= 4500:
    # 80 是填满上一阶梯的固定税额
    print(f"R$ {80 + (s - 3000) * 0.18:.2f}")
else:
    # 350 是填满前两阶梯的固定总税额 (80 + 270)
    print(f"R$ {350 + (s - 4500) * 0.28:.2f}")
