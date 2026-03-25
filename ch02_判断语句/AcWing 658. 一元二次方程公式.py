# -*- coding: utf-8 -*-
"""
@File    : AcWing 658. 一元二次方程公式.py
@Author  : Sgrseven
@Date    : 2026/3/25 21:41
@Link    : https://www.acwing.com/problem/content/660/
"""

a, b, c = map(float, input().split())
d = b ** 2 - 4 * a * c

if a == 0 or d < 0:
    print("Impossivel calcular")
else:
    print(f"R1 = {(-b + d**0.5) / (2 * a):.5f}")
    print(f"R2 = {(-b - d**0.5) / (2 * a):.5f}")
