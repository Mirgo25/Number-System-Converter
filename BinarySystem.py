alphabet = list(map(chr, [i for i in range(ord('A'), ord('Z') + 1)]))
alph_assoc = dict(enumerate(alphabet, 10))
print(alph_assoc)
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
        print("Don't understand")


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
