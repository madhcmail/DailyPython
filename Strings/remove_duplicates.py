# We are given a string and we need to remove all duplicates from it? 
# What will be the output if the order of character matters?

# 1st approach I am using SET() which ensures no duplicates but does not guarantee order
def remove_duplicate(my_string):
    s = set(my_string)
    return ''.join(s)

print(remove_duplicate("geeksforgeeks"))

# 2nd approach - Order gaurantees

def remove_duplicate(my_string):
    s=""
    for char in my_string:
        if char not in s:
            s += char
    return s
print(remove_duplicate("geeksforgeeks"))