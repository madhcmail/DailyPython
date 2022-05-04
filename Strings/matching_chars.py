# Given a pair of non empty strings. 
# Count the number of matching characters in those strings 
# (consider the single count for the character which have duplicates in the strings).

'''
Input : str1 = 'abcdef'
        str2 = 'defghia'
Output : 4 
(i.e. matching characters :- a, d, e, f)
'''

def match_chars(str1, str2):
    count =0
    for char in set(str1):
        if char in set(str2):
            count += 1
    return count
print(match_chars('abcdef','defghia' ))
print(match_chars('aabcddekll12@','bb22ll@55k'))