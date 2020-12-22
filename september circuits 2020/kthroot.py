from math import sqrt
N, K, Q = [int(x) for x in input().split()]

from collections import defaultdict
factors = [None]


if K == 1:
    input()
    for i in range(Q):
        query = [int(x) for x in input().split()]
        
        if query[0] == 1:
            print("Yes")
    
    exit()





def factor(n):
    ans = []
    for i in range(2, 1 + int(sqrt(n))):
        while n % i == 0:
            n //= i
            ans.append(i)
        
        if n == 1:
            break
            
    if n != 1:
        ans.append(n)
    return ans
    
for val in [int(x) for x in input().split()]:

    curr = defaultdict(int)
    
    for i in factor(val):
        curr[i] += 1
        curr[i] %= K
        
    factors.append(curr)




for q in range(Q):
    query = [int(x) for x in input().split()]
    l, r = query[1], query[2]
    
    if query[0] == 1:
        test = defaultdict(int)
        for val in factors[l:r + 1]:
            for k, v in val.items():
                test[k] += v
                test[k] %= K
                
        for k, v in test.items():
            if v:
                print("No")
                break
        else:
            print("Yes")
        
    if query[0] == 2:
        x = query[3]
        y = query[4]
        facts = factor(x)
        y %= K
        if y == 0:
            continue
        
        for val in factors[l:r + 1]:
            for i in facts:
                val[i] += y
                val[i] %= K
    
    if query[0] == 3:
        x = query[3]
        facts = factor(x)
        for val in factors[l:r + 1]:
            for i in facts:
                val[i] += 1
                val[i] %= K
        




    
