"""
4. Написать программу, которая генерирует в указанных пользователем границах:
a) случайное целое число;
b) случайное вещественное число;
c) случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""

from random import randint, uniform


def generator():
    type_selection = input("Введите тип данных: a - целое число, b - вещественное число, c - символ: ")

    if type_selection != 'a' and type_selection != 'b' and type_selection != 'c':
        print(f"Неизвестный тип данных '{type_selection}'")
        return generator()

    initial_value = input("Введите начальное значение: ")
    end_value = input("Введите конечное значение: ")
    try:
        if type(initial_value) != type(end_value):
            print('Типы данных не совпадают. Исправьтесь!')
            return generator()
        elif type_selection == 'a':
            r = randint(int(initial_value), int(end_value))
        elif type_selection == 'b':
            r = uniform(float(initial_value), float(end_value))
        elif type_selection == 'c':
            r = chr(randint(ord(initial_value), ord(end_value)))

        print(f"Случайное значение в диапазоне от {initial_value} до {end_value} = {r}")

    except ValueError:
        print(f"Введенные данные не совпадают с типом '{type_selection}'. Попробуйте еще раз")
        return generator()


generator()
