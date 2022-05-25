# Data hiding: Encapsulation in OOP refers to binding data and the methods 
# to manipulate that data together in a single unit, that is, class.
# No direct access to properties by the code outside of that class.
# Data hiding makes sure that the implementation details are being hidden from the user
# Encapsulating a class, all the properties should be private(__) and 
# any access to the properties should be through methods such as getters and setters.


class Rectangle:
    def __init__(self, length, width):
        self.__length= length
        self.__width= width
    def area(self):
        return self.__length * self.__width
    def perimeter(self):
        return 2 * (self.__length + self.__width)

obj = Rectangle(4,5)
print("Area of a Rectangle= ", obj.area())
print("Perimeter of a Rectange= ", obj.perimeter())
print("length= ", obj.__length)  # this give Attribute Error because the property is defined as private


