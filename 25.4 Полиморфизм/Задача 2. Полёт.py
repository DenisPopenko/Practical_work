class Can_fly():

    def __init__(self, name, height=0, speed=0):
        self.name = name
        self.height = height
        self.speed = speed

    def takeoff(self):
        pass

    def fly(self):
        pass

    def land(self):
        pass

    def __str__(self):
        print('Высота {name} - {height}\nСкорость {name} - {speed}'.format(
            name=self.name, height=str(self.height), speed=str(self.speed)))

class Butterfly(Can_fly):
    def __init__(self, name, height, speed):
        super().__init__(name, height, speed)

    def takeoff(self):
        self.height += 1

    def fly(self):
        self.speed += 0.5

class Rocket(Can_fly):

    def __init__(self, name, height=0, speed=0):
        super().__init__(name, height, speed)

    def takeoff(self):
        self.height += 500
        self.speed += 1000

    def land(self):
        self.height = 0
        print('Взрыв(((')

my_rocket = Rocket('m1')
print(my_rocket)
my_rocket.takeoff()
print(my_rocket)
