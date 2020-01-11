alphabet = list(map(chr, [i for i in range(ord('A'), ord('Z') + 1)]))
alph_assoc = dict(enumerate(alphabet, 10))
print(alph_assoc)


# ----< Фунция преобразования из одной системы счисления в другую >---------------
def dec_to_other(num, base):
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
            result.append('{' + str(quot) + '}')
        else:
            result.append(quot)

        result.reverse()
        return ''.join(map(str, result))
    else:
        return dec_to_other(quot, base)
# -------------------------------------------------------------------------

def other_to_dec():
    pass


# Список для остатков от деления на основу системы счисления
result = []
while True:
    try:
        num = int(input("Enter decimal number: "))
        base = int(input("Enter a base of number system you want to convert your number: "))

        print('The number {} is {} in number system with base of {}'.format(num, dec_to_other(num, base), base))
        break
    except ValueError:
        print("It is not a number! Try again.")
