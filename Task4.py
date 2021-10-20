"""
4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
"""


def sum(n, prev):
    print(prev)
    if n == 1:
        return prev
    else:
        return prev + sum(n - 1, prev * (-0.5))


print(sum(4, 1))
