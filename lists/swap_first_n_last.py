# Python program to swap first and last element of the list.
# Examples: Input : [12, 35, 9, 56, 24]
#           Output : [24, 35, 9, 56, 12]

def swap_ele(my_list):
    first = my_list[0]
    my_list[0] = my_list[-1]
    my_list[-1]= first
    return my_list

print(swap_ele([12,35,9,56,24]))