num_part = int(input('Кол-во участников: '))
num_people = int(input('Кол-во человек в команде: '))

members = []
count = 1

if num_part % num_people != 0:
    print('В командах не равное количество человек.')
else:
    for _ in range(num_part // num_people):
        members.append(list(range(count, count + num_part // num_people + 1)))
        count += num_part // num_people + 1
    print('\nОбщий список команд:', members)