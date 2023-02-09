file = open('people.txt', 'r')
summ = 0
for sym in file:
    if sym.endswith('\n'):
        len_str = len(sym[:-1])
    else:
        len_str = len(sym)
    if len_str < 3:
        raise RuntimeError('Имя менее 2 символов')
    summ += len_str
file.close()
print(summ)