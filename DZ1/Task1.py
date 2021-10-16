"""
1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""


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


calculator()
