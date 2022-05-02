# program to print even length words in a string
''' Input: s = "This is a python language"
    Output: This
            is
            python
            language 
'''

def even_len(my_string):
    new_string = my_string.split()
    for word in new_string:
        if len(word) % 2 ==0:
            print (word)
even_len("This is python language")


