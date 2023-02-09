class Toyota:
    color = 'red'
    price = 1000000
    max_speed = 200
    current_speed = 0

    def info(self):
        print(
            'Цвет {}\nЦена {}\nМаксимальная скорость {}\nТекущая скорость {} км/ч'.format(
            self.color, self.price, self.max_speed, self.current_speed
            )
        )

    def change_cur(self, speed):
        self.current_speed = speed
        print('Текущая скорость автомобиля {} км/ч'.format(self.current_speed))

car_1 = Toyota()
car_1.info()
car_1.change_cur(50)
car_1.info()
print(Toyota.current_speed)