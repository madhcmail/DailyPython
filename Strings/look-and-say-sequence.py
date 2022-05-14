
def get_nextnumber(s):
    i =0
    result = []
    
    while i < len(s):
        count =1
        i = 1
        while i+1 < len(s) and S[i] = s[i+1]:
            i +=1
            count +=1
        result.append(str(count) + s[i])