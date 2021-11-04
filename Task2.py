"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import defaultdict
from functools import reduce


def calc():
    nums = defaultdict(list)

    # defaultdict(<class 'list'>,
    # {'1-A2': ['A', '2'], '2-C4F': ['C', '4', 'F']})
    for i in range(2):
        n = input(f"Введите {i + 1}-е натуральное шестнадцатиричное число: ")
        nums[f"{i + 1}"] = list(n)
    print(nums)

    # 16-указываем с числами какой системы делаем операции
    ressum = sum([int(''.join(i), 16) for i in nums.values()])
    print(nums.values())

    print("Сумма: ", list('%X' % ressum))
    resmul = reduce(lambda a, b: a * b, [int(''.join(i), 16) for i in nums.values()])
    print("Произведение: ", list('%X' % resmul))


#calc()


class HexNumber:
    def __init__(self, num):
        self.num = int(''.join(list(num)), 16)

    def __add__(self, other):
        return list(hex(self.num + other.num))[2:]

    def __mul__(self, other):
        return list(hex(self.num * other.num))[2:]


#n1 = input('Введите первое шестнадцатиричное число: ')
#n2 = input('Введите второе шестнадцатиричное число: ')

n1 = 'A2'
n2 = 'C4F'

print('Результат суммы: ', HexNumber(n1) + HexNumber(n2))
print('Результат произведения: ', HexNumber(n1) * HexNumber(n2))