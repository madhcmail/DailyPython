# find the frequency of maximum occurring character in a python string

from collections import Counter

def max_frequency(my_string):
    res = Counter(my_string)
    print (res)
    return max(res, key = res.get)

print(max_frequency("hello"))


# 2nd approach

def max_frequency_char(my_string):
    res = {}
    for char in my_string:
        if char in res:
            res[char] += 1
        else:
            res[char] = 1
    return max(res, key=res.get)

print(max_frequency_char("hello"))

