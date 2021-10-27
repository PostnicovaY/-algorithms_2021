"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""

from random import random

N = 15
arr = []
for i in range(N):
    arr.append(int(random() * 100) - 50)
print(f'Массив: {arr}')

i = 0
index = -1
while i < N:
    if arr[i] < 0 and index == -1:
        index = i
    elif arr[i] < 0 and arr[i] > arr[index]:
        index = i
    i += 1

print('Значение: %d Позиция в массиве: %d' % (arr[index], index + 1))
