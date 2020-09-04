lookup = {x: {str(y) for y in range(10) if y % x == 0} for x in range(1, 10)}



def count(n, k):
    index = 0
    for i, num in enumerate(reversed(str(n))):
        count = 0
        for j in range(10):
            if j % k == 0:  
                count += 1
            
            if str(j) == num:
                index += (count - 1) * (len(lookup[k]) ** i)
                break
    
    return index
    
def nearest(n, k):
    default = max(lookup[k])
    
    rounded = False
    out = []
    
    for char in str(n):
        if rounded:
            out.append(default)
            continue
        
        if char in lookup[k]:
            out.append(char)
            continue
        
        for i in range(int(char), -1, -1):
            if str(i) in lookup[k]:
                out.append(str(i))
                rounded = True
                break
    return int(''.join(out))
            

    
    
for tc in range(int(input())):
    L, R, k = [int(x) for x in  input().split()]
    
    l, r = nearest(L, k), nearest(R, k)
    
    ans = count(r, k) - count(l, k)
    
    if L == l: ans += 1
    
    print(ans)