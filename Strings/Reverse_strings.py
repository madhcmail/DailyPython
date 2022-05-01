# We are given a string and we need to reverse words of a given string?

# Examples:

# Input : str = geeks quiz practice code
# Output : str = code practice quiz geeks

def rev_sentence(sentence):
    words = sentence.split()
    reversed_sentence = ""
    for word in words[::-1]:
        reversed_sentence += word+" "     
    return reversed_sentence
print(rev_sentence("geeks quiz practice code"))

# without a for loop
# f you need to access individual elements of a list in the reverse order, 
# it's better to use the reversed() function.

def rev_sentence(sentence):
    words = sentence.split()
    reverse_sentence=' '.join(reversed(words))
    return reverse_sentence

if __name__ == "__main__":
    input = "geeks quiz practice code"
    print(rev_sentence(input))
