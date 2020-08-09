N, Q = [int(x) for x in input().split()]

arr = [int(x) for x in input().split()]

for q in range(Q):
    query = [int(x) for x in input().split()]
    
    if query[0]:
        l, r = query[1:]
        if len(set(arr[l - 1:r])) == r - l + 1:
            print('Yes')
        else:
            print('No')
        
        
        
    else:
        arr[query[1] - 1] = query[2]
    