phonebook = {}
while True:
    name = input('\nВведите имя: ')
    surname = input('Введите фамилию: ')
    i_name = (name, surname)
    for i in phonebook:
        if i == i_name:
            print('Этот человек уже есть')
    number = int(input('Введите номер: '))
    phonebook[i_name] = number
    print(phonebook)

# или
# contacts = {}
#
# while True:
#     name = input("Введите имя: ")
#     surname = input("Введите фамилию: ")
#     name_n_surname = (name, surname)
#     if name_n_surname not in contacts:
#         contacts[name_n_surname] = int(input("Введите номер телефона: "))
#     else:
#         print("Такой контакт уже есть!")
#     print(contacts)