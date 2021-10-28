"""
Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""

# Задание 1 урок 1
# В рассчете времени я провела анализ кода 100 раз, и разделила значение на 100, чтобы узнать примерную среднюю скорость кода


# Сложность данного кода O(N) за счет рекурсии, как я думаю

import timeit

code_to_test = """
def calculator():
    try:
        three_digit_number = int(input('Введите трехзначное число или 0 для выхода'))

        if three_digit_number == 0:
            return

        if three_digit_number <= 99 or three_digit_number > 999:
            print('Вы ввели не трехзначное число.')
            return calculator()

        d1 = three_digit_number % 10
        d2 = three_digit_number % 100 // 10
        d3 = three_digit_number // 100
        print("Сумма цифр числа:", d1 + d2 + d3)
        print("Произведение цифр числа:", d1 * d2 * d3)

    except ValueError:
        print('Вы вместо трехзначного числа ввели строку (((. Исправьтесь')

    return calculator()
"""

elapsed_time = timeit.timeit(code_to_test, number=100) / 100
print(f'Время выполнения кода: {elapsed_time}')

# Сложность данного кода O(n^2) за счет цикла

code_to_test_2 = """
number = "123"

sum = 0
prod = 1

for f in number:
    sum += int(f)
    prod *= int(f)
"""

elapsed_time_2 = timeit.timeit(code_to_test_2, number=100) / 100
print(f'Время выполнения кода: {elapsed_time_2}')


