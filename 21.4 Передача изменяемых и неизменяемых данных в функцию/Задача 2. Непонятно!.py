data = input('Введите данные: ')
if str(type(data)) == "<class 'str'>":
    print('Тип данных: str (строка)')
    print('Неизменяемый (immutable)')
    print('Id объекта:', id(data))
elif str(type(data)) == "<class 'dict'>":
    print('Тип данных: dict (словарь)')
    print('Изменяемый (mutable)')
    print('Id объекта:', id(data))
elif str(type(data)) == "<class 'set'>":
    print('Тип данных: set (множество)')
    print('Изменяемый (mutable)')
    print('Id объекта:', id(data))
elif str(type(data)) == "<class 'list'>":
    print('Тип данных: list (список)')
    print('Изменяемый (mutable)')
    print('Id объекта:', id(data))

print(type({'‘a’': 10, '‘b’': 20}))