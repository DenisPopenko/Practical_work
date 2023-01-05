quantity = int(input('Кол-во чисел в списке: '))
numbers = []
for i in range(quantity):
    number = int(input('Введите ' + str(i + 1) + ' число: '))
    numbers.append(number)

divider = int(input('\nВведите делитель: '))
print()

summ_i = 0
index = 0

for i in numbers:
    if i % divider == 0:
        print('Индекс числа' + str(i) + ' : ' + str(index))
        summ_i += index
    index += 1
print('Сумма индексов: ' + str(summ_i))