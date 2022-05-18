# re module allows you to "complie" the expressions that you are searching for frequently.
# This will basically allow you to turn your expreession into a SRE_Pattern object
# you can then use that object in your search function.
# The rprimary reason for compling is to save it to be reused later on in your code.
# However, complie also take some flags that can used to enable various speacila features.
# When you compile patterns, they will get automatically cached 
# so if you aren’t using lot of regular expressions in your code, 
# then you may not need to save the compiled object to a variable.


import re

text = "The ants go marching one by one"
strings = ['the', 'one']

for string in strings:
    regex = re.compile(string)
    print(regex)
    match = re.search(regex,text)
    if match:
        print('Found "{}" in "{}"'.format(string,text))
        text_pos = match.span()
        print(text[match.start():match.end()])
    else:
        print('Did not find "{}"'.format(string))



re.compile('''
           [\w\.-]+      # the user name
           @
           [\w\.-]+'     # the domain
           ''',
           re.VERBOSE)