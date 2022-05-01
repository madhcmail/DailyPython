# Ways to remove ith character in a string

# First Way
def remove_char(my_string,charIndex):
    new_string = ""
    for  i in range(len(my_string)):
        if i == charIndex:
            continue
        else:
            new_string += my_string[i]
    return new_string
print(remove_char("Hello- world", 5))

# second way using replace() string function
# Drawback: if we have same caracter multiple times, it will remove all
# string.replace(oldvalue, newvalue, count) ; count: is optional

def remove_char(my_string,char):
    new_string = my_string.replace(char, '',1)
    return new_string
print(remove_char("Hello--world", '-'))

# Third way: slice and concatenate the ith string

def remove_char(my_string,charIndex):
    new_string = my_string[:charIndex]+my_string[charIndex+1:]
    return new_string
print(remove_char("Hello--world", 5))

# Using str.join() and list comprehension

def remove_char(my_string,charIndex):
    new_string = ''.join([my_string[i] for i in range(len(my_string)) if i != charIndex])
    return new_string
print("The string after removal of ith character: " + remove_char("Hello--world", 5))


