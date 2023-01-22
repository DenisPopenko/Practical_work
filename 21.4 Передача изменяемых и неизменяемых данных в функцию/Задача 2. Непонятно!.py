data = input('Введите данные: ')
if isinstance(data, str):
    print('Тип данных: str (строка)')
    print('Неизменяемый (immutable)')
    print('Id объекта:', id(data))
elif isinstance(data, dict):
    print('Тип данных: dict (словарь)')
    print('Изменяемый (mutable)')
    print('Id объекта:', id(data))

