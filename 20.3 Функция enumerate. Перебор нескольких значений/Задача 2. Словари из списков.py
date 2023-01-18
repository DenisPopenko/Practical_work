import random

abv = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')

# функция формирования списка из алфавита из практики
# def get_random_letter(n):
#     return random.choices([chr(i) for i in range(ord("а"), ord("я"))], k=n)

# print(abv)
first_list = [abv[random.randint(0, 10)] for _ in range(10)]
second_list = [abv[random.randint(0, 10)] for _ in range(10)]
print(f'Первый список: {first_list}\nВторой список: {second_list}\n')

print('Первый словарь:', dict(enumerate(first_list)))
print('Второй словарь:', dict(enumerate(second_list)))
random.c
# dic = {}
# for i, j in enumerate(first_list):
#     dic[i] = j
#     print(dic)
#
# first_dic = hhh(first_list)
# print('Первый словарь:', first_dic)
# print('Второй словарь:', hhh(second_list))
