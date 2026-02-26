# -*- coding: utf-8 -*-
"""
@File    : AcWing 654. 时间转换.py
@Author  : Sgrseven
@Date    : 2026/2/25 20:44
@Link    : https://www.acwing.com/problem/content/656/
"""

time = int(input())
print(f'{time // 3600}:{time % 3600 // 60}:{time % 60}')
