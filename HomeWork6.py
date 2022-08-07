# 1. Создайте программу для игры в "Крестики-нолики".

from random import choice, shuffle


def print_pole(x):  # печать поля
    for i in x:
        for j in i:
            print(player_symbol[j], end='   ')
        print()


def victory_condition(x):  # победные условия
    for i in x:  # проверка одинаковых значений по строкам
        a = i[0]
        if a != 0:
            for j in i[1:]:
                if j != a:
                    break
            else:
                return True, a
    for j in range(len(x[0])):  # проверка одинаковых значений по столбцам
        a = x[0][j]
        if a != 0:
            for i in range(1, len(x)):
                if x[i][j] != a:
                    break
            else:
                return True, a

    diag = x[0][0]
    if diag != 0:
        for i in range(len(x)):
            if x[i][i] != diag:  # проверка одинаковых значений в главной диагонали
                break
        else:
            return True, diag

    reverse_diag = x[0][len(x)-1]
    if reverse_diag != 0:
        for i in range(len(x)):
            # провер. одинак. знач-й в обратной диагонали
            if x[i][len(x)-i-1] != reverse_diag:
                break
        else:
            return True, reverse_diag

    return draw(x), 0


def draw(x):  # проверка на ничью
    for i in x:
        for j in i:
            if j == 0:
                return False
    return True


def bot_player(x, num_player):  # игра бота
    i_index = [0, 1, 2]
    shuffle(i_index)  # рандомное перемешивание списка (не поля)
    for i in i_index:
        row = x[i]  # рандомный вложенный список
        empty_place = []  # список свободных мест в выбранном списке
        for j, k in enumerate(row):
            if k == 0:
                empty_place.append(j)

        if len(empty_place) > 0:
            player_i = i
            player_j = choice(empty_place)  # рандомное число из списка
            return player_i, player_j


def human_player(x, num_player):  # игра человека
    while True:
        print_pole(x)
        x1 = int(input(
            f'Игрок №{num_player}({player_symbol[num_player]}) введите номер строки: '))
        y1 = int(input(
            f'Игрок №{num_player}({player_symbol[num_player]}) введите номер столбца: '))
        if (x1-1) > 2 or (x1-1) < 0 or (y1-1) > 2 or (y1-1) < 0:
            print('Введено некоректное число!')
            continue
        if pole[x1-1][y1-1] > 0:
            print('Это место уже занято!')
            continue
        return x1-1, y1-1


pole = []
player_symbol = '-OX'

player = input('Введите Ваше имя: ')
print(f'{player}, Вы игрок №1')

for i in range(3):  # создание поля 3*3 из нулей
    # temp = []
    # for j in range(3):
    #     temp.append(0)
    temp = [0 for j in range(3)] # с использованием List Comprehension
    pole.append(temp)

current_player = 1
completed_game = False
who_win = 0

while not completed_game:
    if current_player == 1:
        i_index, j_index = human_player(pole, current_player)
        pole[i_index][j_index] = current_player
    elif current_player == 2:
        i_index, j_index = bot_player(pole, current_player)
        pole[i_index][j_index] = current_player

    completed_game, who_win = victory_condition(pole)

    if current_player == 1:
        current_player = 2
    elif current_player == 2:
        current_player = 1

print_pole(pole)

if who_win != 0:
    if who_win == 1:
        print(f'{player}! Победа! Ура!')
    else:
        print(f'Выиграл БОТ!')
else:
    print('Ничья!')


# 2. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,. приоритет операций стандартный.
#   *Пример:
#   2+2 => 4;
#   1+2*3 => 7;
#   1-2*3 => -5;
# - Добавьте возможность использования скобок, меняющих приоритет операций.
#   Пример:
#   1+2*3 => 7;
#   (1+2)*3 => 9;


# в условии задания ограничений по использованию стандартных функций нет, поэтому:
print(eval(input('Введите арифметическое выражение: ')))



# 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


def encoding(x):
    encod = ''
    symbol = ''
    count = ''
    for i in x:
        if i != symbol:
            encod += symbol + str(count)
            count = 1
            symbol = i
        else:
            count += 1
    encod += symbol + str(count)
    return encod


def decoding(x):
    decod = ''
    symbol = ''
    for i in x:
        if i.isalpha():
            symbol = i
        else:
            decod += symbol * int(i)
    return decod


with open('input_encoding.txt', 'r', encoding='utf-8') as file1:
    txt_input_enc = file1.readline()
with open('output_encoding.txt', 'w', encoding='utf-8') as file1_1:
    file1_1.write(encoding(txt_input_enc))

with open('input_decoding.txt', 'r', encoding='utf-8') as file2:
    txt_input_dec = file2.readline()
with open('output_decoding.txt', 'w', encoding='utf-8') as file2_1:
    file2_1.write(decoding(txt_input_dec))
