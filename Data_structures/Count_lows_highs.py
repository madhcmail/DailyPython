# Implement the count_low_high() function. Its parameter is a list of numbers.

# If a number is greater than 50 or divisible by 3, it will count as a high. 
# If these conditions are not met, the number is considered a low.

# At the end of the function, you must return a list that contains 
# the number of lows and highs, in that order. In case the list is empty, 
# you may return None.


def count_low_high(num_list):

    if (len(num_list) == 0):
        return None 
    highs = len([n for n in num_list if n > 50 or n % 3 ==0])
    lows = len([n for n in num_list if n <= 50 and not n % 3 ==0])
    return [lows, highs]

num_list = [20, 9, 51, 81, 50, 42, 77]
print(count_low_high(num_list))
num_list = []
print(count_low_high(num_list))

# Using Filter and lambda
def count_low_high_2(num_list):

    if len(num_list) == 0:
        return None
    high_list = list(filter(lambda num : num > 50 or num % 3 ==0, num_list))
    low_list = list(filter(lambda num : num <= 50 and num % 3 !=0, num_list))

    return [len(low_list), len(high_list)]

num_list = [20, 9, 51, 81, 50, 42, 77]
print(count_low_high_2(num_list))
num_list = []
print(count_low_high_2(num_list))

