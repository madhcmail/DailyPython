#Given two sentences as strings A and B. 
# The task is to return a list of all uncommon words. 
# A word is uncommon if it appears exactly once in any one of the sentences,
# and does not appear in the other sentence.

# Input: A = "Geeks for Geeks"  B = "Learning from Geeks for Geeks"
# Output: ['Learning', 'from']

from collections import Counter
def word_uncommon(str_1, str_2):
    my_string = (str_1+" " + str_2).split()
    result = Counter(my_string)
    return [key for key,val in result.items() if val ==1]

print(word_uncommon("Geeks for Geeks", "Learning from Geeks for Geeks"))
print(word_uncommon("apple banana mango" ,"banana fruits mango"))
