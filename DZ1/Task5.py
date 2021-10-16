"""
5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
"""


def alphabet():
    alphabet_lang = input("Выберите алфавит: a - английский, b - русский, c - арабский: ")

    if alphabet_lang != 'a' and alphabet_lang != 'b' and alphabet_lang != 'c':
        print("Ошибка ввода. Повторите попытку.")
        return alphabet()

    try:
        letter_1 = ord(str(input("Введите первую букву: ")).lower())
        letter_2 = ord(str(input("Введите вторую букву: ")).lower())
        if alphabet_lang == 'a':
            letter_1 = letter_1 - ord('a') + 1
            letter_2 = letter_2 - ord('a') + 1
        elif alphabet_lang == 'b':
            letter_1 = letter_1 - ord('а') + 1  # Внимание, тут указана русская "а"!!!
            letter_2 = letter_2 - ord('а') + 1  # И тут тоже!
        elif alphabet_lang == 'c':
            letter_1 = letter_1 - ord('ﺍ') + 1  # Арабский
            letter_2 = letter_2 - ord('ﺍ') + 1

        print('Позиции: %d и %d' % (letter_1, letter_2))
        print('Между буквами символов:', abs(letter_1 - letter_2) - 1)

    except TypeError:
        print(f"Введенные данные не совпадают с выбранным алфавитом. Попробуйте еще раз")
        return alphabet()


alphabet()
