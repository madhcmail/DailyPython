# A permutation, also called an “arrangement number” or “order”,
#  is a rearrangement of the elements of an ordered list S into a 
# one-to-one correspondence with S itself. A string of length n has n! permutation.

from itertools import permutations

def get_perm(str):
    permlist = permutations(str)
    
    for item in list(permlist):
        print(''.join(item))

get_perm('ABC')