# As set is an unordered collection of data items
# does not allow duplicates
# immutable items (lists, dictionaries) cannot be added

random_set = {"hello", 3.14, (True, False)}
print(random_set)

# length of a set
print(len(random_set))

# set() constructor is another way of creating set.
# Advantage is we can create an empty set

empty_set = set ()
print(empty_set)

random_set = set ({"hello", 3.14, (True, False)})
print(random_set)

# set.add() - single element
# set.update() - multiple items ; input must be a list, tuple or string,

empty_set = set()
empty_set.add(1)
print("The elements in set are: ", empty_set)

empty_set.update([2,3,4,5])
print("The updated set is: ",empty_set)

# Discrad or remove method is to delete an element from set

empty_set.discard(2)
print(empty_set)
empty_set = {(True, False), 3.14, 'hello'}
empty_set.remove((True,False))
print(empty_set)

# Iterate a set using For loop

odd_list = [1,3,5,7]
unorderd_set = {9,11, 13, 15, 17, 19}
print(unorderd_set)

for num in unorderd_set:
    if (not num % 2 == 0):
        odd_list.append(num)
print(odd_list)
