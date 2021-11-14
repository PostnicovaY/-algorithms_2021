"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее)
"""

from random import randint

a = [0] * 10
for i in range(10):
    a[i] = randint(-100, 101)
print(a)


def bubble_sort(array):
    for i in range(len(array) - 1, 0, -1):
        for n in range(i):
            if array[n] > array[n + 1]:
                array[n], array[n + 1] = array[n + 1], array[n]
    return array

print(bubble_sort(a))