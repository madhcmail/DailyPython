# Given a String, perform uppercase of later part of string. 

'''
    Input : test_str = "geeksforgeek"
    Output : geeksfORGEEK
    Explanation : Latter half of string is uppercased.

'''

def half_upper(my_string):
    start_index = len(my_string) // 2
    print(start_index)
    new_string =my_string[:start_index]+my_string[start_index:].upper()
    print(new_string)

half_upper("apples")