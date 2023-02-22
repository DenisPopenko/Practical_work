class Robot:
    def __init__(self, model):
        self.model = model

class Robot_vacuum(Robot):
    def __init__(self, model):
        super().__init__(model)
        self.garbage = 0

    def operate(self):
        print('Робот {} пылесосит'.format(self.model))
        self.garbage += 1
        print('Текущая заполняемость мешка {}'.format(self.garbage))

class Robot_military(Robot):
    def __init__(self, model, weapon):
        super().__init__(model)
        self.weapon = weapon

    def operate(self):
        print('Робот защищает объект с помощью {}'.format(self.weapon))

R1 = Robot_vacuum('q116')
R1.operate()
R2 = Robot_military('w118', 'ракеты')
R2.operate()