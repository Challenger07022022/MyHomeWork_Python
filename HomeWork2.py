# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

def sum_elements(a):
    sp = list(str(a))
    for i in sp:
        if i == '.':
            sp.remove('.')
    sum = 0
    for i in sp:
        sum += int(i)
    return sum


x = (input('Введите вещественное число: '))
try:
    x = float(x)
    print(sum_elements(x))
except:
    print('Введено некорректное число, необходимо вводить только вещественные числа')



# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

from math import factorial


def set_multiplications(n):
    sp = []
    for i in range(1, n+1):
        sp.append(factorial(i))
    return sp


x = int(input('Введите число N: '))
print(set_multiplications(x))

