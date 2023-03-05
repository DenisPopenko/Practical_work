class Unit:
    def __init__(self, name, hp=8):
        self.name = name
        self.hp = hp

    def __str__(self):
        return "Имя: {name}\nУрон {hp}\n".format(name=self.name, hp=self.hp)

class Soldier(Unit):

    def __init__(self, name, hp):
        super().__init__(name)
        self.hp = hp

    def damage(self):
        self.hp -= 1


class Citizen(Unit):

    def __init__(self, name, hp):
        super().__init__(name, hp)

    def damage(self):
        self.hp -= 2


my_soldier = Soldier('Alex', 8)
print(my_soldier)
my_soldier.damage()
print(my_soldier)

my_сitizen = Citizen('Jon', 8)
print(my_сitizen)
my_сitizen.damage()
print(my_сitizen)