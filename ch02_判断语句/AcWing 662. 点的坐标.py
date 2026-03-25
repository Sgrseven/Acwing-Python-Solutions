# -*- coding: utf-8 -*-
"""
@File    : AcWing 662. 点的坐标.py
@Author  : Sgrseven
@Date    : 2026/3/7 23:37
@Link    : https://www.acwing.com/problem/content/664/
"""

x, y = map(float, input().split())

if x > 0 and y > 0:
    print('Q1')
elif x < 0 and y > 0:
    print('Q2')
elif x < 0 and y < 0:
    print('Q3')
elif x > 0 and y < 0:
    print('Q4')
elif x == 0 and y == 0:
    print('Origem')
elif y == 0:
    print('Eixo X')
else:
    print('Eixo Y')
