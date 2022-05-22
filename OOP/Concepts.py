# Objects are a collection of data(propertirs) and their behaviors(methods).
# A class can be thought of as a blueprint for creating objects.
# Example: Lightbulb 
#  -- Properties/state: ON/OFF
# -- Methods/behaviors : turnOn() 
#              turnOff()
# create an object of a class by simply using the name of the class followed by a pair of parenthesis

'''
class MyClass:
    pass

obj = MyClass()  # Creating a MyClass object
print(obj)
'''

from curses.ascii import EM
from sys import set_coroutine_origin_tracking_depth


class Employee:
    # defining properties and Initializing them to none.
    # Initializing the properties in necessary  in class otherwise we get complie errors
    ID = None
    salary = None
    department = None

# ===============================================================================================
# Accessing properties and assigning values#
# To access properties of an object, the dot notation is used:

# object.property
#There are two ways to assign values to properties of a class.

   # Assign values when defining the class.
   # Assign values in the main code.

# Creating an object of the Employee class
Steve = Employee()

Steve.ID = 1234
Steve.salary = 250000
Steve.department = "Human Resources"

print("ID= ", Steve.ID)
print("Salary= ", Steve.salary)
print("department= ", Steve.department)

# Assigning values when defining class

class Student:
    ID = 3456
    name = "Srinika"
    grade = "2nd grade"

student_1 = Student() # creating an object from class

print("Name= ", student_1.name) # accessing the properties of object student_1
print("ID= ", student_1.ID)
print("grade= ", student_1.grade)


# Creating Properties outside of class

class Employee:
    # defining the properties and assigning them None
    ID = None
    salary = None
    department = None


# creating an object of the Employee class
Steve = Employee()

# assigning values to properties of Steve - an object of the Employee class
Steve.ID = 3789
Steve.salary = 2500
Steve.department = "Human Resources"
# creating a new attribute for Steve. This property is for object steve. Any other new objects will
# have only the properties that are declared in the class
Steve.title = "Manager"

# Printing properties of Steve
print("ID =", Steve.ID)
print("Salary", Steve.salary)
print("Department:", Steve.department)
print("Title:", Steve.title)
# ======================================================================================
# Initializer
'''
    Initializer is used to initialize an object of a class. It's a special method that oulines the 
    steps to be performed when an object of a class is created. 
    __init__ is an initialization method and does not have any return type. The first parameter 
    of __init__ is self, which is a way to refer to the object being initialized.
    It is important to define the initializer with complete parameters to avoid any errors.
    Similar to methods, initializers also have the provision for optional parameters.
'''

class School:
    def __init__(self, name,district):
        self.name = name
        self.district = district
school_1 = School('Purple sage', 'RRISD')
school_2 = School('Harmony', 'LISD')

print("name= ", school_1.name)
print("district= ", school_1.district)
print("name= ", school_2.name)
print("name= ", school_2.district)

# Initializer with optional parameters
class School:
    def __init__(self, name,district,location=None):
        self.name = name
        self.district = district
        self.location = location
school_1 = School('Purple sage', 'RRISD','Cedar Park')
school_2 = School('Harmony', 'LISD',)

print("name= ", school_1.name)
print("district= ", school_1.district)
print("Location= ", school_1.location)
print("name= ", school_2.name)
print("name= ", school_2.district)
print("Location= ", school_2.location)


# Class Variables vs Instance Variables

'''
    Class Variables: class variables are shared by all instances or objects of the classes.
    A change in the class variable will change the value of that property in all the objects of the class.

    Instance Variable: instance variables are unique to each instance or object of the class. 
    A change in the instance variable will change the value of the property in that specific object only.
'''
class Player:
    teamName = "LiverPool"

    def __init__(self, name):
        self.name = name
player_1 = Player('Mark')
player_2 = Player('Steve')

print("Name= ", player_1.name)
print("Team= ", player_1.teamName)
print("Name= ", player_2.name)
print("Team= ", player_2.teamName)

# <=============================== Implementing Methods in Class===========================>
'''
A method is a group of statements that performs some operations and may or may not return a result.

3 Types of methods:
1.instance methods
2.class methods
3.static methods

 In Python, the first parameter of the method should ALWAYS be self
'''

class Employee:
    def __init__(self, ID, salary, department):
        self.ID = ID
        self.salary= salary
        self.department= department

    def tax(self):
        return(self.salary * 0.2)
    def salary_per_day(self):
        return(self.salary/30)

steve = Employee(2345, 340000, "Human Resources")

print("ID= ", steve.ID)
print("salary= ", steve.salary)
print("Tax= ", steve.tax())
print("salary per day= ", steve.salary_per_day())


# <==============Class Methods============================>
'''
Class methods work with class variables and are accessible using the class name rather than its object.
Since all class objects share the class variables, class methods are used to access and modify 
class variables.

Syntax:
    To declare a method as a class method, we use the decorator @classmethod.
    cls is used to refer to the class just like self is used to refer to the object of the class. 
'''

class Myclass:
    classVariable = ' Educative'

    @classmethod
    def demo(cls):
        return cls.classVariable

demo_1 = Myclass()
print(demo_1.demo())

class Player:
    teamName = 'Liverpool'

    def __init__(self,name):
        self.name = name
    @classmethod
    def getTeamName(cls):
        return cls.teamName
print(Player.getTeamName())
print(Player.teamName)
player_1 = Player("smith")
print("Name=", player_1.name)


# <==================STATIC Methods ===============================================>
'''
Static methods are methods that are usually limited to class only and not their objects.
They have no direct relation to class variables or instance variables.
They are used as utility functions inside the class or when we do not want the inherited classes  
to modify a method definition.

Static methods can be accessed using the class name or the object name.
'''

class Player:
    teamName='Liverpool'

    def __init__(self,name):
        self.name = name
    
    @staticmethod
    def demo():
        print ("This is a static method")

p1 = Player('lol')
p1.demo()
Player.demo()


#<===============================AccessModifiers========================================================>

'''
Public Attributes: 
Public attributes are those that can be accessed inside the class and outside the class.

Private Attributes:
Private attributes cannot be accessed directly from outside the class but can be accessed from inside the class.
We can make members private using the double underscore __ prefix
'''

# Public Attributes

class Employee:
    def __init__(self, ID, salary):
        # all properties are public
        self.ID = ID
        self.salary = salary

    def displayID(self):
        print("ID:", self.ID)


Steve = Employee(3789, 2500)
Steve.displayID()
print(Steve.salary)

# Private Properties

class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary  # salary is a private property

Steve = Employee(3789, 2500)
print("ID:", Steve.ID)
print("Salary:", Steve.__salary)  # this will cause an error

# Private Methods
class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary  # salary is a private property

    def displaySalary(self):  # displaySalary is a public method
        print("Salary:", self.__salary)

    def __displayID(self):  # displayID is a private method
        print("ID:", self.ID)

Steve = Employee(3789, 2500)
Steve.displaySalary()
Steve.__displayID()  # this will generate an error

# Accessing private attributes in the main code

''' If the user believes it is absolutely necessary to 
access a private property or a method, they can access 
it using the _<ClassName> prefix for the property or method. '''

class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary  # salary is a private property

Steve = Employee(3789, 2500)
print(Steve._Employee__salary)  # accessing a private property