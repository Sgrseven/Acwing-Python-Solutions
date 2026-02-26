# -*- coding: utf-8 -*-
"""
@File    : AcWing 616. 两点间的距离.py
@Author  : Sgrseven
@Date    : 2026/2/25 20:42
@Link    : https://www.acwing.com/problem/content/618/
"""

x1, y1 = map(float,input().split())
x2, y2 = map(float,input().split())
print(f'{((x2 - x1) ** 2+(y2 - y1) ** 2) ** 0.5:.4f}')
