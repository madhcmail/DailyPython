# Given the string, the task is to 
# capitalise the first and last character of each word in a string.

'''
Input: hello world 
Output: HellO WorlD

Input: welcome to geeksforgeeks
Output: WelcomE TO GeeksforgeekS
'''

def capitalize_word(my_string):
    new_string = my_string.split()
    result = ""
    for word in new_string:
        last_element= word[-1].upper()
        result += word[0].upper()+ word[1:len(word)-1]+last_element+' '        
    return result
print(capitalize_word("welcome to geeksforgeeks"))
print(capitalize_word("hello world"))

# 2nd approach
'''
Access the last element using indexing.
Capitalize the first word using title() method.
Then join the each word using join() method.
Perform all the operations inside lambda for writing the code in one-line.
'''

def capitalize_word(s):
    result = ' '.join(map(lambda s:s[:-1]+s[-1].upper(),s.title().split()))
    return result
print(capitalize_word("hello world"))