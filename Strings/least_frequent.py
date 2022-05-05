# find the frequency of minimum occurring character in a python string. 

from collections import Counter
def least_frequency(my_string):
    d = {}
    for key in my_string:
        if key in d:
            d[key] += 1 
        else:
            d[key] = 1

    return min(d, key=d.get)
print(least_frequency("ello"))

# 2nd approach
def least_frequency(my_string):
    print ("The original string: ", my_string)
    res = Counter(my_string)

    return min(res, key=res.get)

print("The minimum of all characters in string ", least_frequency("hello"))