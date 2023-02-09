import random


class Toyota:
    color = 'red'
    price = 1000000
    max_speed = 200
    current_speed = 0

car_1 = Toyota
car_1.current_speed = random.randint(0, 200)
print('Скорость автомобиля {} - {} км/ч'.format('car_1', car_1.current_speed))

car_2 = Toyota
car_2.current_speed = random.randint(0, 200)
print('Скорость автомобиля {} - {} км/ч'.format('car_2', car_2.current_speed))

car_3 = Toyota
car_3.current_speed = random.randint(0, 200)
print('Скорость автомобиля {} - {} км/ч'.format('car_3', car_3.current_speed))