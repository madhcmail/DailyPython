from collections import defaultdict

items = ['a', 'b', 'db', 'd', 'e',
        'a', 'c', 'b', 'a', 'e',
        'bb', 'db', 'aa']

# Find the count of occurances of each item in the array and the item with highest occurance

s = set(items)
print(s)
result= []
for each in s:
    c = items.count(each)
    result.append((each, c))
result.sort(key=lambda x:x[1], reverse=True)
print(result[0])

print ("Ranjith solution")
dic_count = defaultdict(int)
for item in items:
    dic_count[item]+=1
result = sorted(dict(dic_count).items(), key=lambda x:x[1], reverse=True)
print(result)