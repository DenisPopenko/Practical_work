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
        return 'Высота {name} - {height}\nСкорость {name} - {speed}'.format(
            name=self.name, height=self.height, speed=self.speed)

class Butterfly(Can_fly):
    def __init__(self, name, height=0, speed=0):
        super().__init__(name, height, speed)

    def fly(self):
        print('{} летает'.format(self.name))
        self.height = 1
        self.speed = 0.5

class Rocket(Can_fly):

    def __init__(self, name, height=0, speed=0):
        super().__init__(name, height, speed)

    def takeoff(self):
        print('{} взлетела'.format(self.name))
        self.height = 500
        self.speed = 1000

    def land(self):
        self.height = 0
        print('Взрыв(((')

my_rocket = Rocket('m1')
print(my_rocket)
my_rocket.takeoff()
print(my_rocket)

my_butterfly = Butterfly('BI')
print(my_butterfly)
my_butterfly.fly()
print(my_butterfly)
