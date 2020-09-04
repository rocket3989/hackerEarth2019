import numpy as np


N = int(input())

arr = np.array([int(x) for x in input().split()])

idx = np.arange(N)

for Q in range(int(input())):
    
    query = [int(x) for x in input().split()]
    
    if query[0] == 1:
        L, R, x = query[1:]
        
        L -= 1
        R -= 1
        np.add(arr, x, out=arr, where=((idx >= L) & (idx <= R)))
        
        
    elif query[0] == 2:
        L, R, x = query[1:]
        
        L -= 1
        R -= 1
        
        np.multiply(arr, x, out=arr, where=((idx >= L) & (idx <= R)))
        
        
    else:
        x = query[1]
        
        res = np.where(arr == x)
        try:
            print(1 + res[0][-1] - res[0][0])
        except:
            print(-1)
            
    