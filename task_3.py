# task 4
from math import sqrt


class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x} and {self.y}'

    @property
    def coordinat_x(self):
        return self.x

    @property
    def coordinat_y(self):
        return self.y

    @coordinat_x.setter
    def coordinat_x(self, val):
        if not isinstance(val, (int, )):
            raise ValueError('Только числовые значения')
        self.x = val

    @coordinat_y.setter
    def coordinat_y(self, val):
        if not isinstance(val, int):
            raise ValueError('Только числовые значения')
        self.y = val

    def get_distance(self, another_point):
        if not isinstance(another_point, Point):
            raise ValueError('Аргумент должен принадлежать классу Point')
        return sqrt((self.x - another_point.x) ** 2 + (self.y - another_point.y) ** 2)


p1 = Point(5, 4)
p2 = Point(8, 9)
d = p1.get_distance(p2)
# print(p1.get_distance(10))
print(d)
print(p1.coordinat_x)
p1.coordinat_x = 10
print(p1.coordinat_x)
print(p1.get_distance(p2))
p2.coordinat_y = 100
print(p1.get_distance(p2))