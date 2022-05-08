# Problem Statement: Given a list of integers and a number k, 
# find the kth largest integer in the list. 
# The integer will be stored in the kth_max variable.

# Example: with a list of 7 integers, if k = 2, then kth_max will be 
# equal to the second-largest integer in the list. 
# If k = 6, kth_max will equal the 6th largest integer.

test_list= [40,35,82,14,22,66,53]

def kth_largest(test_list,k):
    test_list.sort()
    kth_max = test_list[-k]
    return kth_max

print("The Kth largest Integer: ", kth_largest([40,35,82,14,22,66,53],2))

print("The Kth largest Integer: ", kth_largest([40,35,82,14,22,66,53],6))