# -*- coding: utf-8 -*-
"""
@File    : AcWing 657. 选择练习1.py
@Author  : Sgrseven
@Date    : 2026/3/7 22:00
@Link    : https://www.acwing.com/problem/content/659/
"""

a, b, c, d = map(int, input().split())
print('Valores aceitos' if b > c and d > a and c + d > a + b and c > 0 and d > 0 and not(a % 2) else 'Valores nao aceitos')
