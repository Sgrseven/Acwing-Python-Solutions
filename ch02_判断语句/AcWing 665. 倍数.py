# -*- coding: utf-8 -*-
"""
@File    : AcWing 665. 倍数.py
@Author  : Sgrseven
@Date    : 2026/3/7 12:16
@Link    : https://www.acwing.com/problem/content/667/
"""

a, b = map(int,input().split())
print('Sao Multiplos' if a % b == 0 or b % a == 0 else 'Nao sao Multiplos')
