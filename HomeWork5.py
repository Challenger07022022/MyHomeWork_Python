# 1. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов. Это не просто сумма всех коэффициентов.
# Сумма многочленов равна многочлену, членами которого являются все члены данных многочленов.
# например, в 1 файле было 3*x^3 + 5*x^2+10*x+11, в другом 7*x^2+55
# то в итоге будет, 3*x^3 + 12*x^2+10*x+66


# декомпозиция текста в словарь, key = степень : value = коэффициент
def decomposition(x):
    dictionary = {}
    txt = x.replace(' ', '').split('+')
    for i in txt:
        if '^' in i:
            a = i.split('^')
            dictionary[int(a[1])] = int(a[0].split('*')[0])
        elif '*' in i:
            a = i.split('*')
            dictionary[1] = int(a[0])
        else:
            dictionary[0] = int(i)
    return dictionary

# суммирование значений словарей с одинаковыми ключами (степенью)
def sum_polynomials(x, y):
    dictionary = y.copy()
    for k, v in x.items():
        try:
            dictionary[k] += v
        except:
            dictionary[k] = v
    sorted_dictionary = dict(sorted(dictionary.items(), reverse=True))
    return sorted_dictionary

# преобразование словаря в исходный вид
def composition(x):
    a = []
    for k, v in x.items():
        if k == 1:
            a.append(f'{v}x')
        elif k == 0:
            a.append(f'{v}')
        else:
            a.append(f'{v}x^{k}')
    b = "+".join(a)
    return b


# чтение строки из файлов
with open('polynomial1.txt', 'r') as file1:
    txt1 = file1.readline()
with open('polynomial2.txt', 'r') as file2:
    txt2 = file2.readline()

a, b = decomposition(txt1), decomposition(txt2)
c = sum_polynomials(a, b)

# создание и запись результата в файл:
with open('sum_polynomial_1_2.txt', 'w') as file3:
    file3.write(composition(c))


# 2. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность.
# Порядок элементов менять нельзя.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]
# [1, 5, 2, 3, 4, 1, 7] => [1, 5]

def increasing_sequence(x):
    # sp1, sp2 = [], []
    # for i in x:
    #     if i-1 in x or i+1 in x:
    #         sp1.append(i)
    # sp2.append(min(sp1))
    # sp2.append(max(sp1))
    # return sp2
    sp1 = [i for i in x if i-1 in x or i+1 in x]
    sp2 = []
    sp2.append(min(sp1))
    sp2.append(max(sp1))
    return sp2

a = [1, 5, 2, 3, 4, 6, 1, 7]
b = [1, 5, 2, 3, 4, 1, 7]
print(increasing_sequence(a))
print(increasing_sequence(b))
