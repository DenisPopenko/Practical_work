str = input('Строка: ')
print('Ответ:', end = ' ')
for i, j in enumerate(str):
    if j == '~':
        print(i, end = ' ')
