# Given String list, extract frequency of specific characters in whole strings list.
# Input : test_list = [“geeksforgeeks is best for geeks”], chr_list = [‘e’, ‘b’, ‘g’, ‘f’]
# Output : {‘g’: 3, ‘e’: 7, ‘b’: 1, ‘f’ : 1}

from collections import Counter
char_list = ['e', 'b', 'g', 'f']
output = {}
def char_frequency(my_list, char_list):
    for each_str in my_list:
        char_count = Counter(each_str)
        for char in char_list:
            if char in char_count.keys():
                output[char]= char_count[char]
    return output

print(char_frequency(["geeksforgeeks is best for geeks", "hello"], ['e', 'b', 'g', 'f','h']))

# 2nd Approach with dict comprehension + Counter()

from collections import Counter
char_list = ['e', 'b', 'g', 'f']
test_list = ["geeksforgeeks is best for geeks"]
res = {key:val for key,val in dict(Counter("".join(test_list))).items() if key in char_list}

print("The frequency of specific chars: ", res)