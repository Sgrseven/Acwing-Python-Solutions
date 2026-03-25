# -*- coding: utf-8 -*-
"""
@File    : AcWing 668. 游戏时间2.py
@Author  : Sgrseven
@Date    : 2026/3/8 12:25
@Link    : https://www.acwing.com/problem/content/670/
"""

a, b, c, d = map(int, input().split())

# 将时间全部转换为分钟并作差
diff = c * 60 + d - a * 60 - b

# 如果 diff <= 0，说明跨天或刚好满 24 小时，补上一天的总分钟数 (1440)
print(f"O JOGO DUROU {diff // 60} HORA(S) E {diff % 60} MINUTO(S)" if diff > 0 else f"O JOGO DUROU {(diff + 1440) // 60} HORA(S) E {(diff + 1440) % 60} MINUTO(S)")
