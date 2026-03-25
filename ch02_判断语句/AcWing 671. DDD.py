# -*- coding: utf-8 -*-
"""
@File    : AcWing 671. DDD.py
@Author  : Sgrseven
@Date    : 2026/3/7 17:45
@Link    : https://www.acwing.com/problem/content/673/
"""

ddd_map = {
    61: "Brasilia", 71: "Salvador", 11: "Sao Paulo", 21: "Rio de Janeiro",
    32: "Juiz de Fora", 19: "Campinas", 27: "Vitoria", 31: "Belo Horizonte"
}
print(ddd_map.get(int(input()), "DDD nao cadastrado"))
