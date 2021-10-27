"""
4. Определить, какое число в массиве встречается чаще всего.
"""

from random import random

N = 15
arr = [0] * N
for i in range(N):
    arr[i] = int(random() * 20)
print(f'Массив: {arr}')

num = arr[0]
max_frq = 1
for i in range(N - 1):
    frq = 1
    for k in range(i + 1, N):
        if arr[i] == arr[k]:
            frq += 1
    if frq > max_frq:
        max_frq = frq
        num = arr[i]

if max_frq > 1:
    print('Число - %d встречается - %d раз(а)' % (num, max_frq))
else:
    print('Все элементы уникальны')
