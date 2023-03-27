from typing import Callable, Any

class Robot:

    def __init__(self, model: any):
        self.model = model

    def mes(self):
        print('Я - робот!')


class Drone(Robot):

    def __init__(self, model: str, height: int, speed: int):
        super().__init__(model)
        self.height = height
        self.speed = speed

    def takeoff(self, height):
        print(f'Дрон {self.model} взлетел на высоту {height} метров')

    def flight(self, speed):
        print(f'Дрон {self.model} летит со скоростью {speed} километров в час')

    def landing(self):
        print(f'Дрон {self.model} приземлился')
        self.height = 0

class Reconnaissance_drone(Drone):

    def __init__(self, model: any, height: int, speed: int):
        super().__init__(model, height, speed)

    def operate(self):
        print(f'{self.model} - веду разведку с воздуха')

class Military_drone(Drone):

    def __init__(self, model: any, height: int, speed: int, weapon: str):
        super().__init__(model, height, speed)
        self.weapon = weapon

    def operate(self):
        print(f'{self.model} - веду защиту военного объекта с воздуха с помощью {self.weapon}')


drone1 = Reconnaissance_drone('C1', 100, 50)
drone2 = Military_drone('C2', 80, 35, 'топольМ')

drone1.takeoff(80)
drone1.flight(50)
drone1.operate()
drone1.landing()
print()
drone2.takeoff(80)
drone2.flight(35)
drone2.operate()
drone2.landing()