# -*- coding: utf-8 -*-
"""
@File    : AcWing 664. 三角形.py
@Author  : Sgrseven
@Date    : 2026/3/7 22:27
@Link    : https://www.acwing.com/problem/content/666/
"""

a, b, c = map(float, input().split())
print(f'Perimetro = {a + b + c :.1f}'if a + b > c and a + c > b and b + c > a else f'Area = {(a + b ) * c / 2:.1f}')
