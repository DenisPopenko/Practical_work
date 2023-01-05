name = input('Введите имя: ')
num = int(input('Введите номер заказа: '))

res = 'Здравствуйте, {h}! Ваш номер заказа: {k}. Приятного дня!'.format(h=name, k=num)
print(res)