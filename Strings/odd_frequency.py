# Odd Frequency Characters

from collections import Counter

def odd_frequency(my_string):    
    result = Counter(my_string)
    output = []
    for key, value in result.items():
        if value % 2 != 0:
            output.append(key)
        else:
            continue
    return [key for key, value in result.items() if value % 2 !=0]
print(odd_frequency("hello"))

# 2nd approach : list comprehension way

def odd_frequency_2(my_string):
    result = Counter(my_string)
    return [key for key, value in result.items() if value % 2 !=0]

print(odd_frequency_2("hello"))