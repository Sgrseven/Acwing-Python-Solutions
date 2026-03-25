# -*- coding: utf-8 -*-
"""
@File    : AcWing 660. 零食.py
@Author  : Sgrseven
@Date    : 2026/3/7 12:43
@Link    : https://www.acwing.com/problem/content/662/
"""

x, y = map(int, input().split())
print(f'Total: R$ {[0, 4, 4.5, 5, 2, 1.5][x] * y:.2f}')
