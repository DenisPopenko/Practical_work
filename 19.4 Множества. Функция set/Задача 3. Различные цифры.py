lst = set(input('Введите строку: '))
lst_num = set()
for i in lst:
    if '0' <= i <= '9':
        lst_num.add(i)
print('Различные цифры строки:', ''.join(lst_num))

