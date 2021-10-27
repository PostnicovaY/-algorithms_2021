"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random

N = 15
arr = [0] * N
for i in range(N):
    arr[i] = random.randint(0, 99)
print(f'Массив: {arr}')

mn = min(arr)
mx = max(arr)
imn = arr.index(mn)
imx = arr.index(mx)
print('Минимальное число - %d Максимальное число - %d' % (mn, mx))
arr[imn], arr[imx] = arr[imx], arr[imn]

print(f'Массив: {arr}')
