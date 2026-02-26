# -*- coding: utf-8 -*-
"""
@File    : AcWing 614. 最大值.py
@Author  : Sgrseven
@Date    : 2026/2/26 18:17
@Link    : https://www.acwing.com/problem/content/616/
"""

a, b, c = map(int, input().split())
max_ab = (a + b + abs(a - b)) / 2
print(f'{(max_ab + c + abs(max_ab - c)) / 2:.0f} eh o maior')
