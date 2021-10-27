"""
Вот тут при вставке условия задания выдает ошибку ¯\_(ツ)_/¯
"""

import random

N = 5

first_array = [0] * N
array_index = []

for i in range(N):
    first_array[i] = random.randint(0, 99)
    if first_array[i] % 2 == 0:
        array_index.append(i)

print('Первый массив: ', first_array)
print('Индексы четных элементов: ', array_index)
