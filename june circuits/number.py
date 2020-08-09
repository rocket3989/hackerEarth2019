from math import gcd, comb
def nCr(n, r): 
  
    p = 1
    k = 1
    
    if (n < r): 
        return 0
  
    if (r != 0):  
        while (r): 
            
            p *= n 
            k *= r 
  
            m = gcd(p, k) 
  
            p //= m 
            k //= m 
  
            n -= 1
            r -= 1
    else: 
        p = 1
  
    return p

from collections import defaultdict

for tc in range(int(input())):
    n, l = [int(x) for x in input().split()]
    counts = [0 for i in range(30)]

    for val in [int(x) for x in input().split()]:
        pos = 0
        while val:
            if val & 1:
                counts[pos] += 1 << pos
            val >>= 1
            pos += 1
        
    condensed = defaultdict(int)
    for val in counts:
        if val:
            condensed[val] += 1
    
    for val, count in reversed(sorted(condensed.items())):
        if count < l:
            l -= count
        elif count == l: 
            print(1)
            break
        else:
            print(nCr(count, l))
            break
    else:
        print(-1)