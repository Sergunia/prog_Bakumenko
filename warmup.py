from abc import *


class Shape:
    def __init__(self, width, height, name):
        self.name = name
        self.width = width
        self.height = height

    def print(self):
        print(self.name, "площадь", self.area())

    @abstractmethod
    def area(self):
        pass


class Triangle(Shape):
    def __init__(self, width, height):
        super().__init__(width, height, "Треугольник")

    def area(self):
        return int(self.width * self.height / 2)


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__(width, height, "Прямоугольник")

    def area(self):
        return self.width * self.height


t = Triangle(30, 10)
t.print()
r = Rectangle(30, 10)
r.print()