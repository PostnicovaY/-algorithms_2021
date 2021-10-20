"""
2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""


def numbers(n):
    if n == 0:
        return [0, 0]

    current = n % 10
    next = numbers(n // 10)

    if current % 2 == 0:
        return [next[0] + 1, next[1]]
    else:
        return [next[0], next[1] + 1]


print(numbers(40567322))
