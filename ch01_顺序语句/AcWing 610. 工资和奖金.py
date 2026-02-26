# -*- coding: utf-8 -*-
"""
@File    : AcWing 610. 工资和奖金.py
@Author  : Sgrseven
@Date    : 2026/2/26 18:14
@Link    : https://www.acwing.com/problem/content/612/
"""

from sys import stdin
a, b = map(float, stdin.readlines()[1:])
print(f'TOTAL = R$ {a + b * 0.15:.2f}')
