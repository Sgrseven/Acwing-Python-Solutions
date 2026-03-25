# -*- coding: utf-8 -*-
"""
@File    : AcWing 667. 游戏时间.py
@Author  : Sgrseven
@Date    : 2026/3/7 17:46
@Link    : https://www.acwing.com/problem/content/669/
"""

a, b = map(int, input().split())

if a < b:
    print(f"O JOGO DUROU {b - a} HORA(S)")
else:
    print(f"O JOGO DUROU {24 + b - a} HORA(S)")
