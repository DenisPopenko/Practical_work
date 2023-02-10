class Potato:
    states = {0: 'Осутствует', 1 : 'Росток' , 2 : 'Зелёная', 3 : 'Зоелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def print_state(self):
        print('Картошка {} сейчас {}'.format(
            self.index, Potato.states[self.state]
        ))

class PotatoGarden:
    def __init__(self, count):
        self.potates = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка растёт')
        for i_potato in self.potates:
            i_potato.grow()

    def are_all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potates]):
            print('Картошка ещё не созрела!\n')
        else:
            print('Вся картошка созрела. Можно собирать!\n')

my_garden = PotatoGarden(5)
my_garden.are_all_ripe()

