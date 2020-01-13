alphabet = list(map(chr, [i for i in range(ord('A'), ord('Z') + 1)]))
alph_assoc = dict(enumerate(alphabet, 10))
print(alph_assoc)
alph_assoc_inv = dict(zip(alph_assoc.values(), alph_assoc.keys()))
print(alph_assoc_inv)
flag: bool = False
ch: str = ""
# Список для остатков от деления на основу системы счисления
result = []


# ----< Фунция преобразования из десятичной системы счисления в другую >---------------
def dec_to_other(num, base):
    num = int(num)
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
        return ''.join(map(str, result))
    else:
        return dec_to_other(quot, base)
# ------------------------------------------------------------------------------------


# ----< Фунция преобразования из одной системы счисления в десятичную >---------------
def other_to_dec(num, base):
    if 2 <= base <= 36:
        return int(num, base)
    else:
        if '.' in num:          # Если вещественное число



            print('Dot is here!!!!')



        else:                   # Если целое число

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

            num = map(num_from_letter, num)               # Конвертируем все буквы в числа
            num = filter(None, map(del_brackets, num))    # Удаляем скобки из списка
            num = list(map(int, num))                     # Преобразуем в тип данных int
            num.reverse()
            index_num = list(range(0, len(num)))        # Список индексов цифр в числе
            num = list(map(lambda i, number: number * pow(base, i), index_num, num))
            return sum(num)
            # for number in num:
            #     num[i+1] = number * pow(base, i+1)
# ------------------------------------------------------------------------------------


# ---------------------------< Аналог switch-case >-----------------------------------
def switch(num, base_in, base_out):
    switcher = {
        10: dec_to_other
    }
    func = switcher.get(base_in, lambda num, base_in: other_to_dec(num, base_in))
    if base_in == 10:
        return func(num, base_out)
    else:
        return func(num, base_in)
# ------------------------------------------------------------------------------------

# ---------------------------< Главный цикл программы >-----------------------------------
while True:
    try:
        num = input("Enter a number: ")
        base_in = int(input("Enter a number system of entered number: "))
        base_out = int(input("Enter a base of number system you want to convert your number: "))
        print('The number {} in {} number system is {} in number system with base of {}'.format
                        (num,  base_in,   switch(num, base_in, base_out),         base_out))
        break
    except ValueError:
        print("It is not a number! Try again.")
# ------------------------------------------------------------------------------------