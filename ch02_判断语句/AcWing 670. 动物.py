# -*- coding: utf-8 -*-
"""
@File    : AcWing 670. 动物.py
@Author  : Sgrseven
@Date    : 2026/3/25 21:50
@Link    : https://www.acwing.com/problem/content/672/
"""

import sys

a, b, c = sys.stdin.read().split()

if a == "vertebrado":
    if b == "ave":
        print("aguia" if c == "carnivoro" else "pomba")
    else:
        print("homem" if c == "onivoro" else "vaca")
else:
    if b == "inseto":
        print("pulga" if c == "hematofago" else "lagarta")
    else:
        print("sanguessuga" if c == "hematofago" else "minhoca")
