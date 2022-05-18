def less_than_ten(x):
    return x < 10

my_list = [1,2,3,10,23,24]
for item in filter(less_than_ten, my_list):
    print(item)


# map built-in

def doubler(x):
    return x*2

my_list = [1, 2, 3, 20, 30]
for item in map(doubler, my_list):
    print(item)
print(list(map(doubler,my_list)))