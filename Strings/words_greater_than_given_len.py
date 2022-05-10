# A string is given, and you have to find all the 
# words (substrings separated by a space) which are greater than the given length k.

# Input : str = "hello geeks for geeks is computer science portal" 
 #       k = 4
# Output : hello geeks geeks computer science portal
# Explanation : The output is list of all words that are of length more than k.

def words_greater(my_string, klen):
    
    words_split= my_string.split()
    return [word for word in words_split if len(word) > klen]

print(words_greater("hello geeks for geeks is computer science portal", 4))
print(words_greater("string is fun in python",3))