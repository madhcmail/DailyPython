# Given a String, compute all the characters, except spaces.
def avoid_spaces(my_string):
    mystr_list = my_string.split(' ')
    new_string=''
    for word in mystr_list:
        new_string += word
        print(new_string)
    return len(new_string)

print(avoid_spaces('Hello world'))

# second possible way using  sum(),map(), len(),split()
# map() function creates a map object using an existing list and function as it parmeters
# map(function, list)

def avoid_spaces(my_string):
    res = sum(map(len, my_string.split()))
    return res
print(avoid_spaces('Hello world'))