# -*- coding: utf-8 -*-
"""
@File    : AcWing 656. 钞票和硬币.py
@Author  : Sgrseven
@Date    : 2026/2/26 18:18
@Link    : https://www.acwing.com/problem/content/658/
"""

n = float(input()) * 100
print('NOTAS:')
for i in [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]:
    if i == 1: print('MOEDAS:')
    print(f"{int(n // (i * 100))} {'nota(s)' if i > 1 else 'moeda(s)'} de R$ {i:.2f}")
    n %= (i * 100)
