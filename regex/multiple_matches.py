# findall function will search through the string you pass and find each match to a list
# finditer function find matches but it is a iterator function where you needto iterata to get the output 


import re

silly_string ="the cat in the hat"
pattern = "the"

print(re.findall(pattern,silly_string))

for match in re.finditer(pattern,silly_string):
    print(match)
    print ("Found '{group} at '{begin}':'{end}''".format(group=match.group(),begin=match.start(),end=match.end()))
    
