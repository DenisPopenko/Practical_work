class Point:
    __count = 0

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
        Point.__count += 1

    def __str__(self):
        return self.__x, self.__y


    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

t = Point(2, 5)
m = Point(5, 6)
print(t.get_x(), t.get_y())
print(m.get_x(), m.get_y())
x = 1
y = 2
print(f'{set(str(x))}, {set(str(y))}')


