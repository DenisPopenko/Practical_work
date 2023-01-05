quantity = int(input('\nКол-во сотрудников: '))
staff = []
for i in range(quantity):
    #print('Зарплата', i + 1, 'сотрудника: ', end = '')
    salary = int(input(f"Зарплата {i + 1} сотрудника: "))
    if salary != 0:
        staff.append(salary)

print('\nОсталось сотрудников:', len(staff))
print('Зарплаты:', staff)

print('\nМаксимальная зп:', max(staff))
print('Максимальная зп:', min(staff))