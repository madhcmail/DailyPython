# Inheritance provides a way to create a new class from an existing class.
# This new class is a specialized version of Parent class where it inherits all non-private feilds and methods
# of existing class
# Whenever you have a IS A replationship we implement Inheritance.
# Parent Class (Super class or Base Class):This class allows the reuse of its public properties in another class.
# Child Class (Sub class or Derived class): This class inherits or extends the superclass.

# Example

class Vehicle:
    def __init__(self, make, model, color):
        self.make = make
        self.model=model
        self.color=color
    def PrintDetails(self):
        print("Make= ", self.make)
        print("Model= ", self.model)
        print("color= ", self.color)

class Car(Vehicle):
    def __init__(self, make, model, color, Doors):
        # calling the parent constructor
        Vehicle.__init__(self, make, model,color)
        self.Doors = Doors
    def printCarDetails(self):
        self.PrintDetails()
        print("Doors= ",self.Doors)

obj = Car("Honda","Civic","Grey",4)
obj.PrintDetails()
obj.printCarDetails()


# -------- Super Function and it's 3 uses ---------------------
# 1. super() is used when the Parent class and Child class have same property names and if you want
    # to refer to parent class you can use super()
# 2. super() is used when the methods names is same in parent and child class and if you want to
    # refer to parent class methods, we use super()
# 3. when you are initialzling the parent class properties in child class

class Vehicle:
    fuelcap = 90
    
class Car(Vehicle):

    def setfuelcap(self, fuelcap):
        self.fuelcap = fuelcap
       
    def printDetails(self):
        print("Parent class Fuel Cap= ", super().fuelcap)
        print("Car Fulecap= ", self.fuelcap)

obj = Car()
obj.setfuelcap(50)
obj.printDetails()