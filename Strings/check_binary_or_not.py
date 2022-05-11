# Check if a given string is binary string or not
# Input: str = "01010101010"
# Output: Yes

# Input: str = "geeks101"
# Output: No

from tabnanny import check


def check_binary(my_string):
    p = set(my_string)
    s = {'0','1'}
    if s == p or p == {'0'} or p =={'1'}:
        return "YES"
    else:
        return "NO"


print(check_binary("0101101"))
