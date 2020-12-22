import numpy as np

n, m = [int(x) for x in input().split()]

arr = np.array([int(x) for x in input().split()])

for q in range(m):

    query = [int(x) for x in input().split()]
    
    l, r = query[1:3]
    l -= 1
    r -= 1
    
    if query[0] == 1:
        arr[l:r + 1] = query[-1]    
        
    if query[0] == 2:
        np.gcd(arr[l:r + 1], query[-1], out=arr[l:r + 1])
        
    if query[0] == 3:
        print(np.amax(arr[l:r + 1]))
    
    if query[0] == 4:
        print(np.sum(arr[l:r + 1]))