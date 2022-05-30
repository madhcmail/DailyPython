import re

def search_url(my_string):
    str = re.search('[https]+',my_string)
    text_pos= str.span()
    print(text_pos)
    return (my_string[str.start():str.end()])

print(search_url("My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles "))


text = "Hello world10"
match = re.search('[\s]+',text)
print(match)