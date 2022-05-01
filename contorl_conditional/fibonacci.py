# 0 1 1 2 3 5 8
fib_list=[]
def fib(num):

    for i in range(num):
        if i == 0:
            fib_list.append(0)
        elif i == 1:
            fib_list.append(1)
        else:
            value = fib_list[i-1]+fib_list[i-2]
            fib_list.append(value)
    return(fib_list[num -1])

print(fib(6))
