# def numb(num):
#     if num > 255:
#         print('Ошибка ввода, чсило должно быть менее, либо равно 255.')
#
#
#
# num_1 = int(input('Введите первное число: '))
# numb(num_1)
# num_2 = int(input('Введите второе число: '))
# numb(num_2)
# num_3 = int(input('Введите третье число: '))
# numb(num_3)
# num_4 = int(input('Введите четвертое число: '))
# numb(num_4)
# print('{0}.{1}.{2}.{3}'.format(num_1, num_2, num_3, num_4))

ip_address = "{0}.{1}.{2}.{3}"
numbers = []

for i in range(4):
    new_numbers = int(input(f'Введите {i + 1} число: '))
    if 0 <= new_numbers <= 255:
        numbers.append(new_numbers)
    else:
        print('Ошибка ввода, чсило должно быть менее, либо равно 255.')
        break

print(ip_address.format(numbers[0], numbers[1], numbers[2], numbers[3]))

