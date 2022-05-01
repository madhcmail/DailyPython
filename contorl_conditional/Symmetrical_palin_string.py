# Example: khakha
# symmetrical: if both the halves of the string are the same
# Palindrome:  if one half of the string is the reverse of the other half or 
# if a string appears same when read forward or backward.
'''Input: khokho
Output: 
The entered string is symmetrical
The entered string is not palindrome

Input:amaama
Output:
The entered string is symmetrical
The entered string is palindrome '''

def check_symmetry(my_string):
    if len(my_string) % 2 == 0:
        indice = len(my_string)//2
        print(indice)
        first_half = my_string[0:indice]
        second_half = my_string[indice: ]
        if first_half == second_half:
            print("The entered string is symmetry")
        else:
            print("The entered string is not symmetry")

check_symmetry("khakho")

def check_palindrome(my_string):
    rev_mystring = my_string[::-1]
    print(rev_mystring)
    if my_string == rev_mystring:
        print("The entered string is Palindrome")
    else:
        print("The entered string is not palindrome")

check_palindrome("amaama")
