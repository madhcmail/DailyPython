from collections import Counter, defaultdict, deque

counter_one = "superfulous"

print(Counter(counter_one))

items = ['a', 'b', 'db', 'd', 'e',
        'a', 'c', 'b', 'a', 'e',
        'bb', 'db', 'aa']

counter = Counter(items)
print(counter.most_common(2))

sentence = "The red for jumped over the fence and ran to the zoo for food"

words = sentence.split()
d = defaultdict(int) # by defaut each key is set to 0
for word in words:
    d[word] += 1
print(d)

my_list = [(1234, 100.23), (345, 10.45), (1234, 75.00),
           (345, 222.66), (678, 300.25), (1234, 35.67)]

reg_dict = {}
for acc_num, value in my_list:
    if acc_num in reg_dict:
        reg_dict[acc_num].append(value)
    else:
        reg_dict[acc_num] = [value]
print(reg_dict)

# 2nd approach using defaultdict

my_list = [(1234, 100.23), (345, 10.45), (1234, 75.00),
           (345, 222.66), (678, 300.25), (1234, 35.67)]
d = defaultdict(list)
for acc_num,value in my_list:
    d[acc_num].append(value)
print(d)

items = ['a', 'b', 'db', 'd', 'e',
        'a', 'c', 'b', 'a', 'e',
        'bb', 'db', 'aa']

d = defaultdict(int)
for letter in items:
    d[letter] += 1

result = sorted(dict(d).items(), key=lambda x:x[1], reverse=True)
print(result[0])

d = deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])

d.append("Hello")
print(d)
right = d.pop()
print(right)
print(d.popleft())

items = deque([],3)

items.append(4)
items.append(5)
items.append(6)
items.append(7)
print(list(items))

