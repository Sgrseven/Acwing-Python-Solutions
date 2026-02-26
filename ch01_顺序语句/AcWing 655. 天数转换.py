# -*- coding: utf-8 -*-
"""
@File    : AcWing 655. 天数转换.py
@Author  : Sgrseven
@Date    : 2026/2/26 18:19
@Link    : https://www.acwing.com/problem/content/657/
"""

n = int(input())
print(f'{n //365} ano(s)',f'{n % 365 // 30} mes(es)',f'{n %365 % 30} dia(s)',sep = '\n')
