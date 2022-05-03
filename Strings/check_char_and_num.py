# Given a string in Python. The task is to check whether the string
#  has at least one letter(character) and one number. Return “True” 
#  if the given string full fill above condition else return “False” (without quotes).


def check_string(my_string):
    letter = False
    number = False
    for s in my_string:
        if s.isalpha():
            letter= True
        elif s.isdigit():
            number= True
    return letter and number

print(check_string("stringwithoutnum23"))
print(check_string("welcometoourcountry"))
            
            