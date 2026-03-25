# -*- coding: utf-8 -*-
"""
@File    : AcWing 663. 简单排序.py
@Author  : Sgrseven
@Date    : 2026/3/7 17:46
@Link    : https://www.acwing.com/problem/content/665/
"""

nums = list(map(int, input().split()))
print(*sorted(nums), sep='\n')
print()
print(*nums, sep='\n')
