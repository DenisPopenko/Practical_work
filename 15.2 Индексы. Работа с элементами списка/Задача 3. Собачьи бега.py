quantity = int(input('Кол-во собак: '))
list_points = []

for i in range(quantity):
    point = int(input(f'Введите очки {i + 1} собаки: '))
    list_points.append(point)

print(list_points)

max_point = list_points[0]
min_point = list_points[0]
i = 0
i_max = 0
i_min = 0

for points in list_points:
    if points > max_point:
        max_point = points
        i_max = i
    elif points < min_point:
        min_point = points
        i_min = i
    i += 1

list_points[i_min], list_points[i_max] = list_points[i_max], list_points[i_min]

print(list_points)


