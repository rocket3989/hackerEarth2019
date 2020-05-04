def firstLarger(look, val):
    val += 1
    l, r = 0, len(look) - 1
    
    while l != r:
        mid = (l + r) // 2
        
        if look[mid] < val:
            l = mid + 1
        else:
            r = mid
    return l
    
def firstSmaller(look, val):
    val -= 1
    l, r = 0, len(look) - 1
    
    while l != r:
        mid = (l + r + 1) // 2
        
        if look[mid] > val:
            r = mid - 1
        else:
            l = mid
    return l    
    
    
N, M = [int(x) for x in input().split()]

arr = [int(x) for x in input().split()]

counts = [0] + [int(x) for x in input().split()]

lookup = [[] for i in range(M + 1)]


for i, val in enumerate(arr):
    lookup[val].append(i)

skip = set()
for i, look in enumerate(lookup):
    if len(look) == 0:
        skip.add(i)

for q in range(int(input())):
    l, r = [int(x) for x in input().split()]
    
    
    for i, count in enumerate(counts):
        if i in skip: continue
        
        
        lPos = firstLarger(lookup[i], l)
        rPos = firstSmaller(lookup[i], r)
        
        if rPos <= lPos: continue
        
        if (rPos - lPos) + 1 != count:
            print(0)
            break
         
    else:
        print(1)
