# Given a string, the task is to check if that string contains any special character (defined special character set). 
# If any special character found, don’t accept that string.

def check_special_char(my_string):
    
    if my_string.replace(' ','').isalnum():
        return "String is Accepted"  
    else:
        return "String is Not Accepted"

print(check_special_char("Geeks$For$Geeks"))
print(check_special_char("Geeks For Geeks"))