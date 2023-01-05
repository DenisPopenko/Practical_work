first_message = input('Первое сообщение: ')
second_message = input('Второе сообщение: ')

first_list = list(first_message)
second_list = list(second_message)

k_first = first_list.count('!') + first_list.count('?')
k_second = second_list.count('!') + second_list.count('?')

if k_first > k_second:
    print(first_message, second_message)
elif k_second > k_first:
    print(second_message, first_message)
else:
    print('Ой!')