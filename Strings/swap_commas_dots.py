# Given a string, we need to replace all commas with dots and all dots with the commas. 

'''
    Input : 14, 625, 498.002
    Output : 14.625.498, 002 
''' 

def swap_str(my_string):
    new_string=""
    for char in my_string:
        if char == ',':
            new_string += '.'
        elif char == '.':
            new_string += ','+' '
        elif char == ' ':
            new_string += ''
        else:
            new_string += char
    return new_string

print(swap_str("14, 625, 498.002"))


# 2nd approach: use Translat() and maketrans()
'''
The translate() method returns a string where some specified characters are
 replaced with the character described in a dictionary, or in a mapping table.
Use the maketrans() method to create a mapping table.
If a character is not specified in the dictionary/table, the character will not be replaced.
If you use a dictionary, you must use ascii codes instead of characters.
'''

def Replace(str):
    maketrans = str.maketrans
    print(maketrans)
    final = str.translate(maketrans(',.','.,',' '))
    return final.replace(',',', ')

print(Replace("14, 625, 498.002"))