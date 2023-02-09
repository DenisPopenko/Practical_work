class Family:
    surname = 'Common family'
    money = 100000
    hause = False

    def info(self):
        print(self.surname, self.money, self.hause)

    def earn_money(self, amount):
        self.money += amount

    def buy_house(self, price, discount=0):
        price -= price * discount / 100
        if self.money >= price:
            print('Семья приобрела дом')
            self.money -= price
            self.hause = True
        else:
            print('Не хватает денег')

my_family = Family()
my_family.info()
my_family.buy_house(500000)
my_family.earn_money(350000)
my_family.buy_house(500000, 10)
my_family.info()