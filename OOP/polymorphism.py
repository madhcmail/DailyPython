# The word Polymorphism is a combination of two Greek words, Poly meaning many and Morph meaning forms.
# polymorphism refers to the same object exhibiting different forms and behaviors.

class Shape:
    def __init__(self):
        self.sides = 0
    def getArea(self):
        pass
class Rectangle(Shape):
    def __init__(self, width=0, length=0):
        self.sides = 4
        self.width = width
        self.length = length
    def getArea(self):
        return self.width * self.length
class Circle(Shape):
    def __init__(self, radius=0):
        self.radius = radius
    def getArea(self):
        return (self.radius * self.radius * 3.14)

shapes = [Rectangle(3,4), Circle(5)]
print("Rectangle Area: ", shapes[0].getArea())
print("Circle sides= ", shapes[1].getArea())