def add(n1,n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2


def  calculator(operation, n1, n2):
    return operation(n1, n2)

result = calculator(multiply, 10, 20)
print(result)
print(calculator(add,45,15))


# using lambda function. Lambda functions can be passed as aruguments

result = calculator(lambda n1,n2 : n1*n2, 10,20)
print(result)

#filter

num_list = [20, 30, 5, -20, 12]

greater_than_10 = list(filter((lambda num : num > 10), num_list))

print(greater_than_10)


