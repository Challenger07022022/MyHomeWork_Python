# 1. Задайте список. Напишите программу, которая определит, присутствует ли
# в заданном списке строк некое число.

def find_text(x, spisok):
    a = 'NO'
    for i in spisok.split():
        if i == x:
            a = 'YES'
    return a


sp = input('Введите текст: ')
number = input('Введите некое число: ')
print(find_text(number, sp))


# 2. Напишите программу, которая определит позицию второго вхождения строки
# в списке либо сообщит, что её нет.
# Пример:
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1


def position_second_entry(x, spisok):
    entry = 0
    position = -1
    j = -1
    for i in spisok:
        j += 1
        if i == x:
            entry += 1
            if entry == 2:
                position = j
    return position


sp = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
print(position_second_entry('qwe', sp))
sp = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
print(position_second_entry('йцу', sp))
sp = ["йцу", "фыв", "ячс", "цук", "йцукен"]
print(position_second_entry('йцу', sp))
sp = ["123", "234", 123, "567"]
print(position_second_entry('123', sp))
sp = []
print(position_second_entry(123, sp))


# 3* (необзательная).
# Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком
# количестве используется в этой книге.
# Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова,
# разделённые пробелом и вывести получившуюся статистику.
# Программа должна считывать одну строку со стандартного ввода и выводить для каждого уникального
# слова в этой строке число его повторений (без учёта регистра) в формате "слово количество" (см. пример вывода).
# Порядок вывода слов может быть произвольным, каждое уникальное слово﻿ должно выводиться только один раз.
# Sample Input 1:
# a aa abC aa ac abc bcd a
# Sample Output 1:
# ac 1
# a 2
# abc 2
# bcd 1
# aa 2
# Sample Input 2:
# a A a
# Sample Output 2:
# a 3


def quantity_recurring_words(spisok):
    text = spisok.lower().split()
    dictionary = {}

    for i in text:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    return dictionary

a = input('Введите текст: ')
b = quantity_recurring_words(a)
for i in b:
    print(i, b[i])
