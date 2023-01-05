start = int(input('Левая граница: '))
stop = int(input('Правая граница: '))

print(f'\nСписок кубов чисел в диапазоне от {start} до {stop}: {[x ** 3 for x in range(start, stop + 1)]}')
print(f'Список квадратов чисел в диапазоне от {start} до {stop}: {[x ** 2 for x in range(start, stop + 1)]}')