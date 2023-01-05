import random

q_num = int(input('Введите длину списка: '))
q_lst = [random.randint(0, q_num) for _ in range(q_num)]
print(q_lst)
del_start = int(input('Начальный индекс: '))
del_end = int(input('Конечный индекс: '))

q_lst = q_lst[:del_start - 1] + q_lst[del_end:]
print(q_lst)