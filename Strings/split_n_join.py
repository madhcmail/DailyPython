# Split a string based on a delimiter and join the string using another delimiter.

# Input : Geeks for Geeks
# Output : Geeks-for-Geeks

def string_split(my_string,delimeter):
    new_string= delimeter.join(my_string.split())

    return new_string
print(string_split("Geeks for Geeks", '-'))