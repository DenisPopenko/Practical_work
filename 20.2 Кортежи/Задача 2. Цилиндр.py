import math
def geom(r, h):
    side = 2 * math.pi * r * h
    S = 2 * math.pi * r ** 2
    full = side + 2 * S
    return side, full

radius = int(input('Введите радиус: '))
height = int(input('Введите высоту: '))

a, b = geom(radius, height)
print(a, b)
#или
print(f'Площадь боковой поверхности цилиндра: {geom(radius, height)[0]}')
print(f'Полная площадь: {geom(radius, height)[1]}')


