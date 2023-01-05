new_ID_numbers = []
employees = int(input('Кол-во сотрудников в офисе: '))
for _ in range(employees):
    ID_number = int(input('ID сотрудника: '))
    new_ID_numbers.append(ID_number)

search_id = int(input("Какого сотрудника ищем? "))

search = False
for id in new_ID_numbers:
    if id == search_id:
        search = True

if search:
    print("Сотрудник работает!")
else:
    print("Сотрудник не работает!")

#или

if search_id not in new_ID_numbers:  # Благодаря оператору in поиск можно упростить
    print("Сотрудник не работает!")
else:
    print("Сотрудник работает!")