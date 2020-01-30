alphabet = list(map(chr, [i for i in range(ord('A'), ord('Z') + 1)]))
alph_assoc = dict(enumerate(alphabet, 10))
print(alph_assoc)
alph_assoc_inv = dict(zip(alph_assoc.values(), alph_assoc.keys()))
print(alph_assoc_inv)
flag: bool = False
trigger: bool = True
ch: str = ""
# Список для остатков от деления на основу системы счисления \ Список для целых остатков от умножения на основу системы счисления
result, fractResult = [], ['.']


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



def other_to_dec(num, base):
    """Фунция преобразования из одной системы счисления в десятичную."""

    def num_from_letter(x):  # Функция, которая конвертирует букву в число
        if x in alph_assoc.values():
            number = str(alph_assoc_inv[x])
            return number
        else:
            return x

    def del_brackets(x):    # Функция, которая удаляет из списка скобки и записывает, что было внутри, 1-им числом.
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

    if '.' not in num and 2 <= base <= 36:
        return int(num, base)
    else:
        if '.' in num:          # Если вещественное число
            intNum, fractNum = num.split('.')  # Разделяем на целую и дробную части вещественное число
            intNum, fractNum = map(num_from_letter, intNum), map(num_from_letter,
                                                                 fractNum)  # Конвертируем все буквы в числа
            intNum, fractNum = filter(None, map(del_brackets, intNum)), filter(None, map(del_brackets,
                                                                                         fractNum))  # Удаляем скобки из списка
            intNum, fractNum = list(map(int, intNum)), list(map(int, fractNum))  # Преобразуем в тип данных int
            intNum.reverse(), fractNum.reverse()
            index_intNum, index_fractNum = list(range(0, len(intNum))), list(
                range(-len(fractNum), 0))  # Список индексов цифр в числе
            intNum = list(map(lambda i, number: number * pow(base, i), index_intNum, intNum))
            fractNum = list(map(lambda i, number: number * pow(base, i), index_fractNum, fractNum))
            return sum(intNum + fractNum)

        else:                   # Если целое число
            num = map(num_from_letter, num)               # Конвертируем все буквы в числа
            num = filter(None, map(del_brackets, num))    # Удаляем скобки из списка
            num = list(map(int, num))                     # Преобразуем в тип данных int
            num.reverse()
            index_num = list(range(0, len(num)))        # Список индексов цифр в числе
            num = list(map(lambda i, number: number * pow(base, i), index_num, num))
            return sum(num)


def other_to_other(num, base_in, base_out):
    """
    Функция преобразования чисел с одной системы счисления(СС) в другую.

    :param num: str - Число, которое нужно преобразовать.
    :param base_in: int - Основа СС, в которой введено число.
    :param base_out: int - Основа СС, в которую надо преобразовать число.
    """
    if base_in == 10:           # Сработает если перевести в одну и ту же СС
        return dec_to_other(num, base_out)
    elif base_out == 10:
        return other_to_dec(num, base_in)
    else:
        return dec_to_other(str(other_to_dec(num, base_in)), base_out)


# ---------------------------< Главный цикл программы >-----------------------------------
while True:
    try:
        num = input("Enter a number: ")
        base_in = int(input("Enter a number system of entered number: "))
        base_out = int(input("Enter a base of number system you want to convert your number: "))
        print('The number {} in {} number system is {} in number system with base of {}'.format
                        (num,  base_in,   other_to_other(num, base_in, base_out),         base_out))
        break
    except ValueError:
        print("It is not a number! Try again.")
# ------------------------------------------------------------------------------------