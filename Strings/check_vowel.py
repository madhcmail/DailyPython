# Given a string, the task is to check if every vowel is present or not. 
# We consider a vowel to be present if it is present in upper case or lower case. 
# i.e. ‘a’, ‘e’, ‘i’.’o’, ‘u’ or ‘A’, ‘E’, ‘I’, ‘O’, ‘U’ .

def check_vowel(my_string):
    s = set()
    for i in range(len(my_string)):
        if my_string[i] in ['a','e','i','o','u'] or my_string[i] in ['A','E','I','O','U']:
            s.add(my_string[i].upper())
    if len(s) ==5:
        return  "Accepted"
    else:
        return "Not Accepted"

print(check_vowel("ABeeIghiObhkUul"))
print(check_vowel("geeksforgeeks"))