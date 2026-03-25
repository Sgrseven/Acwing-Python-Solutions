# -*- coding: utf-8 -*-
"""
@File    : AcWing 661. 平均数3.py
@Author  : Sgrseven
@Date    : 2026/3/25 21:58
@Link    : https://www.acwing.com/problem/content/663/
"""

n1, n2, n3, n4 = map(float, input().split())
x = (n1 * 2 + n2 * 3 + n3 * 4 + n4) / 10

print(f"Media: {x:.1f}")

if x >= 7:
    print("Aluno aprovado.")
elif x < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    y = float(input())  # 读取补考成绩
    print(f"Nota do exame: {y:.1f}")

    z = (x + y) / 2
    print("Aluno aprovado." if z >= 5 else "Aluno reprovado.")
    print(f"Media final: {z:.1f}")
