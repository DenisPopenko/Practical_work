class Ship:

    def __init__(self, model):
        self.model = model

    def info(self):
        print('Модель: ', self.model)

    def movement(self):
        print('Корабль {} движется'.format(self.model))

class СargoShip(Ship):
    def __init__(self, model, workload=0):
        super().__init__(model)
        self.workload = workload

    def load(self):
        print('Загружаем корабль')
        self.workload += 1
        print('Текущая загруженность - {}'.format(self.workload))

    def unload(self):
        print('Разгружаем корабль')
        if self.workload > 0:
            self.workload -= 1
        else:
            print('Корабль уже разгружен')
        print('Текущая загруженность - {}'.format(self.workload))

class WarShip(Ship):
    def __init__(self, model, weapon):
        super().__init__(model)
        self.weapon = weapon

    def attac(self):
        print('Корабль атакует при помощи {}'.format(self.weapon))


ship1 = СargoShip('c-16')
ship1.load()
ship2 = WarShip('w-17', 'ракеты')
ship2.attac()


