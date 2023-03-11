import random

class Iter():

    def __init__(self, count):
        self.count = count
        self.number = 0
        self.cur_val = 0

    def __iter__(self):
        self.number = 0
        return self

    def __next__(self):
        self.count -= 1
        if self.count == 0:
            raise StopIteration
        self.cur_val += random.uniform(0, 1)

        return self.cur_val

my_iter = Iter(5)
for i in my_iter:
    print(i)



