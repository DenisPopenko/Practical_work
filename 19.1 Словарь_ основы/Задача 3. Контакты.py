contacts = dict()
#print('Текущие контакты на телефоне:\n', contacts)
while True:
    print('\nТекущие контакты на телефоне:')
    for i in contacts:
        print(i, contacts[i])
    name = input('\nВведите имя: ')
    number = int(input('Введите номер телефона: '))
    contacts[name] = number
