class Point:
    count = 0

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        Point.count += 1

    def info(self):
        print(self.x, self.y)

t = Point(2, 5)
m = Point(5, 6)
t.info()
m.info()
print(t.count)