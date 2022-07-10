# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

def DeterminantWeekends(x):
    if x > 7 or x < 1:
        return 'Введено некорректное число, необходимо ввести число от 1 до 7'
    elif x >= 6:
        return 'да'
    else:
        return 'нет'

z = input('Введите день недели цифрой: ')
try:
    z = int(z)
    print(DeterminantWeekends(z))
except:
    print('Введено некорректное число, необходимо ввести целое число от 1 до 7')


# 2.изучить понятие Предикатов.

# Изучено!


# 3. Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится
# эта точка (или на какой оси она находится).
# *Пример:*
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def FindQvart(x, y):
    if (x > 0 and y > 0):
        return 1
    elif (x < 0 and  y > 0):
        return 2
    elif (x < 0 and  y < 0):
        return 3
    elif (x > 0 and  y < 0):
        return 4
    else:
        return 'Координата не должна быть равна 0'

n = input('Введите координату точки x: ')
m = input('Введите координату точки y: ')
try:
    n = float(n)
    m = float(m)
    print(FindQvart(n, m))
except:
    print('Введены некорректные данные, необходимо вводить только цифры')