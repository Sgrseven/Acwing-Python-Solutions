# -*- coding: utf-8 -*-
"""
@File    : AcWing 653. 钞票.py
@Author  : Sgrseven
@Date    : 2026/2/25 20:43
@Link    : https://www.acwing.com/problem/content/655/
"""

n = int(input())
print(n)
l = [100, 50, 20, 10, 5, 2, 1]
for i in range(0, len(l)):
    print(f'{n // l[i]} nota(s) de R$ {l[i]},00')
    n = n % l[i]
