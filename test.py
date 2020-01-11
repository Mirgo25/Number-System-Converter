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
# a=14
# if a in lst:
#     print(a)
#     print(lst[a])

# Testing list with strings and numbers
"""
a_lst = [123, 214, 324, 'asd', 'asdcczxc', '23411', 23947]
b_lst = map(str, a_lst)
print(list(b_lst))
"""

