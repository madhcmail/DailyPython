# Implement the check_sum() function which takes in a list and returns 
# True if the sum of two numbers in the list is zero.
# If no such pair exists, return False.

def check_sum(num_list):
    for i in num_list:
        for j in num_list:
            if  i + j == 0:
                return True
    return False
                
 
print(check_sum([10,-14,26,5,-3,13,-5]))
print(check_sum([10,-14,26,5,-3]))