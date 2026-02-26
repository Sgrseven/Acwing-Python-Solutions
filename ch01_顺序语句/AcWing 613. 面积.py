# -*- coding: utf-8 -*-
"""
@File    : AcWing 613. 面积.py
@Author  : Sgrseven
@Date    : 2026/2/26 14:29
@Link    : https://www.acwing.com/problem/content/615/
"""

a, b, c = map(float, input().split())
print(f'TRIANGULO: {a * c / 2:.3f}',f'CIRCULO: {3.14159 * c ** 2:.3f}',f'TRAPEZIO: {(a + b) * c / 2:.3f}',f'QUADRADO: {b ** 2:.3f}',f'RETANGULO: {a * b:.3f}',sep = '\n')
