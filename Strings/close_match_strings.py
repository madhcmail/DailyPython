# Find all close matches of input string from a list
# given a list of pattern strings and a single input string. We need to find all possible close good enough 
# matches of input string into list of pattern strings.

# Input : patterns = ['ape', 'apple', 'peach', 'puppy'], 
        # input = 'appel'
# Output : ['apple', 'ape']

# difflib.get_close_matches(word, possibilities, n, cutoff) accepts four parameters 
# in which n, cutoff are optional. word is a sequence for which close matches are 
# desired, possibilities is a list of sequences against which to match word. 
# Optional argument n (default 3) is the maximum number of close matches to return, 
# n must be greater than 0. Optional argument cutoff (default 0.6) is a float in the 
# range [0, 1]. Possibilities that don’t score at least that similar to word are 
# ignored. The best (no more than n) matches among the possibilities 
# are returned in a list, sorted by similarity score, most similar first.


# Function to find all close matches of 
# input string in given list of possible strings
from difflib import get_close_matches

def close_match(patterns,word):
    output = get_close_matches(word, patterns)
    return output

if __name__ == "__main__":
    pattern = ['ape', 'apple', 'peach', 'puppy']
    word = 'appel'
    print(close_match(pattern,word))