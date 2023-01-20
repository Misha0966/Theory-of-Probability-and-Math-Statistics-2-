# Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8.
# Стрелок выстрелил 100 раз.
# Найдите вероятность того, что стрелок попадет в цель ровно 85 раз.
# 
# Используя биномиальное распределение
# Количество сочетаний из 100 по 85 
# умножаем на вероятность одного попадания в степени количества предполагаемых попаданий (0.8 в степени 85)
# умножаем на вероятность одного непопадания в степени количества предполагаемых неудач (0.2 в степени 15)
# Получим вероятность = 0.048


from math import factorial
import numpy as np
n = 100 # число испытаний
k = 85 # кол-во благоприятных исходов
p = 0.8 # вероятность события

def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

c = combinations(n, k)

# биномиальное распределение

P = c * p**k * 0.2**15

# Ответ: 0.048061793700746556, или 4.8%