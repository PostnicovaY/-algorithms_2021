"""
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, то надо вывести число 6843.
"""


def reverse(n):
    current = n % 10
    future = n // 10
    if n == 0:
        return ""
    else:
        return str(current) + str(reverse(future))


print(reverse(12340))
