# -*- coding: utf-8 -*-
"""
@File    : AcWing 666. 三角形类型.py
@Author  : Sgrseven
@Date    : 2026/3/25 21:47
@Link    : https://www.acwing.com/problem/content/668/
"""

a, b, c = sorted(map(float, input().split()), reverse=True)

if a >= b + c:
    print("NAO FORMA TRIANGULO")
else:
    if a ** 2 == b ** 2 + c ** 2:
        print("TRIANGULO RETANGULO")
    elif a ** 2 > b ** 2 + c ** 2:
        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    elif a == b or b == c:
        print("TRIANGULO ISOSCELES")
