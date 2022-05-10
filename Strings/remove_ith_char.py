# we have to remove the ith indexed character from the string.

# In any string, indexing always start from 0.
# Example: Input = "Geeks" 
#           i=1
#           Output = "Geks"

def remove_ith(my_string, ith):
    new_string = my_string[:ith]+my_string[ith+1:]
    return new_string

print(remove_ith("Geeks",1))

# 2nd approach 
# string.replace(oldvalue, newvalue, count)

def remove_ith_char(my_string, i):
    new_string = my_string.replace(my_string[i], '',1)
    return new_string
print(remove_ith_char("Geeks",1))