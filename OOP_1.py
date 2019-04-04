class Shape:
    def __init__ (self, height, width):
        self.height = height
        self.width = width

class Triangle(Shape):
    def area(self):
        return 0.5*self.height*self.width

class Rectangle(Shape):
    def area(self):
        return self.height*self.width

t = Triangle(10, 15)
r = Rectangle(20, 20)
print (t.area())
print (r.area())
