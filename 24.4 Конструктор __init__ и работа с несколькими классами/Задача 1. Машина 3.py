class Toyota:

    def __init__(self, color, price, max_speed):
        self.color = color
        self.price = price
        self.max_speed = max_speed
        self.current_speed = 0

    def info(self):
        print(
            'Цвет {}\nЦена {}\nМаксимальная скорость {}\nТекущая скорость {} км/ч'.format(
                self.color, self.price, self.max_speed, self.current_speed
            )
        )

    def change_cur(self, speed):
        self.current_speed = speed
        print('Текущая скорость автомобиля {} км/ч'.format(self.current_speed))

car_1 = Toyota('red', 1000000, 200)
car_1.info()
car_1.change_cur(50)
car_1.info()
print(car_1.current_speed)