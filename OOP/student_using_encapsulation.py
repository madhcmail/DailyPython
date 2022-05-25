class Student:
    def __init__(self, name=None, rollno=None):
        self.__name = name
        self.__rollno = rollno
    def getName(self):
        return self.__name
    def getRollno(self):
        return self.__rollno
    def setName(self, name):
        self.__name = name
    def setRollno(self, rollno):
        self.__rollno = rollno

student_1 = Student("Madhuri", 1203)
print("Student_1 Info")
# print(student_1.__name) # give attribute error
print(student_1.getName())

student_2 = Student()
student_2.setName("Srinika")
student_2.setRollno(2345)

print("student_2 Info")

print(student_2.getName())
print(student_2.getRollno())