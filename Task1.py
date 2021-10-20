"""
1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и снова запрашивать знак операции. Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.
"""


def calculator():
    inquiry = input('Введите операцию (+, -, *, / или 0 для выхода)')

    if inquiry == '0':
        return

    if inquiry != '+' and inquiry != '-' and inquiry != '*' and inquiry != '/' and inquiry != '0':
        print('Вы ввели неверную операцию.')
        return calculator()

    try:
        first_num = int(input('Введите первое число: '))
        second_num = int(input('Введите второе число: '))

        if inquiry == '/' and second_num == 0:
            print('На ноль делить нельзя!')
            return calculator()

        if inquiry == '+':
            result = first_num + second_num
            print('Ваш результат:', result, '\n')
        elif inquiry == '-':
            result = first_num - second_num
            print('Ваш результат:', result, '\n')
        elif inquiry == '*':
            result = first_num * second_num
            print('Ваш результат:', result, '\n')
        elif inquiry == '/':
            result = first_num / second_num
            print('Ваш результат:', result, '\n')

    except ValueError:
        print('Вы вместо числа ввели строку (((. Исправьтесь')

    return calculator()


calculator()
