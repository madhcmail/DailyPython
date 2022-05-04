# Given a string, count the number of vowels present in given string using Sets.
'''
Input : GeeksforGeeks
Output : No. of vowels : 5

Input : Hello World
Output : No. of vowels :  3
'''

s = set("aeiouAEIOU")
def count_vowel(my_string):
    count = 0
    for char in my_string:
        if char in s:
            count += 1
    return count
print(count_vowel("GeeksforGeeks"))
print(count_vowel("Hello World"))
            
