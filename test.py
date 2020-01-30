# Преобразуем строку из чисел, фиг. скобок и букв только числа
alphabet = list(map(chr, [i for i in range(ord('A'), ord('Z') + 1)]))
alph_assoc = dict(enumerate(alphabet, 10))
print(alph_assoc)
alph_assoc_inv = dict(zip(alph_assoc.values(), alph_assoc.keys()))
print(alph_assoc_inv)
flag: bool = False
trigger: bool = True
ch: str = ""
num = '135.734538'  # 135489785.68
base = 10      # 35
result, fractResult = [], ['.']

'''
# ----< Фунция преобразования из десятичной системы счисления в другую >---------------
def dec_to_other(num, base):
    """Фунция преобразования из десятичной системы счисления в другую."""
    global trigger

    if trigger == True:
        if '.' in num:
            i = 0
            fractNum = num.split('.')[1]
            fractNum = float(fractNum)/pow(10, len(fractNum))
            while True:
                product = fractNum * base
                intPart = int(product)     # Целая часть числа от умножения на вещественное число (оно идет в результат)
                fractNum = float('{:.6f}'.format(product - intPart))    # Дробная часть числа от умножения на вещ. число \
                                                                        # 21.08 - 21.00 = 0.0799999999999983 \
                                                                        # поэтому использую float('{:.5f}'.format(product - intPart))
                i += 1
                if intPart in alph_assoc:
                    fractResult.append(alph_assoc[intPart])
                elif intPart > max(alph_assoc.keys()):
                    # если число выходит за диапазон алфавита, оно берется в фиг. скобки,\
                    # и считается отдельным числом в выбранной системе счисления
                    fractResult.append('{' + str(intPart) + '}')
                else:
                    fractResult.append(intPart)
                if product - intPart == 0.0 or i == 10:            # Условие завершения цикла
                    break
            # num = float(num)
            trigger = False
        else:
            trigger = False
            fractResult.clear()
            # num = int(num)
    num = int(float(num))
    quot = num // base
    rest = num % base
    if rest in alph_assoc:
        result.append(alph_assoc[rest])
    elif rest > max(alph_assoc.keys()):
        # если число выходит за диапазон алфавита, оно берется в фиг. скобки,\
        # и считается отдельным числом в выбранной системе счисления
        result.append('{' + str(rest) + '}')
    else:
        result.append(rest)
    if base > quot:
        if quot in alph_assoc:
            result.append(alph_assoc[quot])
        elif quot > max(alph_assoc.keys()):
            # если число выходит за диапазон алфавита, оно берется в фиг. скобки,\
            # и считается отдельным числом в выбранной системе счисления
            result.append('{' + str(quot) + '}')
        else:
            result.append(quot)

        result.reverse()
        result.extend(fractResult)
        return ''.join(map(str, result))
    else:
        return dec_to_other(quot, base)
# ------------------------------------------------------------------------------------

print(dec_to_other(num, base))
'''


'''
def num_from_letter(x):  # Функция, которая конвертирует букву в число
    if x in alph_assoc.values():
        number = str(alph_assoc_inv[x])
        return number
    else:
        return x


def del_brackets(x):  # Функция, которая удаляет из списка скобки и записывает, что было внутри, 1-им числом
    global flag
    global ch
    if '{' == x:
        ch = ''
        flag = True
        # return None
    elif flag == True:
        if '}' == x:
            flag = False
            return ch
        else:
            ch = ch + x
            # return None
    else:
        return x
# Ниже для вещественных числе в num
intNum, fractNum = num.split('.')   # Разделяем на целую и дробную части вещественное число
intNum, fractNum = map(num_from_letter, intNum), map(num_from_letter, fractNum)  # Конвертируем все буквы в числа
intNum, fractNum = filter(None, map(del_brackets, intNum)), filter(None, map(del_brackets, fractNum))  # Удаляем скобки из списка
intNum, fractNum = list(map(int, intNum)), list(map(int, fractNum))  # Преобразуем в тип данных int
intNum.reverse(), fractNum.reverse()
index_intNum, index_fractNum = list(range(0, len(intNum))), list(range(-len(fractNum), 0))  # Список индексов цифр в числе
intNum = list(map(lambda i, number: number * pow(base, i), index_intNum, intNum))
fractNum = list(map(lambda i, number: number * pow(base, i), index_fractNum, fractNum))
print(sum(intNum + fractNum))
#----------------------------------------------------------------------------------

# Ниже для целых чисел в num
num1 = list(map(num_from_letter, num))  # Конвертируем все буквы в числа
num2 = list(map(del_brackets, num1))
num3 = list(filter(None, num2))  # Удаляем скобки из списка
num4 = list(map(int, num3))  # Преобразуем в тип данных int
num4.reverse()
index_num = list(range(0, len(num4)))        # Список индексов цифр в числе
num5 = list(map(lambda i, number: number * pow(base, i), index_num, num4))
print(sum(num5))
#----------------------------------------------------------------------------------
'''

# x = 1231233211
# print('{:,}'.format(x).replace(',', ' '))

# print("Units destroyed: {players[0]!r:/>30}".format(players = ['1', '2', '3']))

'''
# Testing alphabet with corresponding numbers
a = list()
num = 4
numAlphabet = [i for i in range(ord('A'), ord('Z')+1)]
print(numAlphabet)
alphabet = list(map(chr, numAlphabet))
print(alphabet)

alph_assoc = dict(enumerate(alphabet, 10))
print(alph_assoc)
print(max(alph_assoc.keys()))

a.append('{'+str(num)+'}')
print(a)

print(int('ee', 17))
'''
# a=14
# if a in lst:
#     print(a)
#     print(lst[a])

"""
# Testing list with strings and numbers
a_lst = [123, 214, 324, 'asd', 'asdcczxc', '23411', 23947]
b_lst = map(str, a_lst)
print(list(b_lst))
"""

