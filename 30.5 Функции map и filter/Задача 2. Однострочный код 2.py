# Введите строку: qWe456rtY
# ['q', 'e', 'r', 't']

lst = input('Введите строку: ')
print(list(filter(lambda x: not (x.isupper() or x.isdigit()), lst)))