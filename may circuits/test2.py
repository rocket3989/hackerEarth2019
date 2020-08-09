
from collections import defaultdict

n = int(input())


# for val in primes:
#     prime = val
#     if prime >= n:
#         break
        
prime = 5003

arrays = [list(range(1 + 2 * prime, 2 * (1 + 2 * prime + n), 2)), list(range(prime + 1, 2 * (prime + 1 + n), 2)), list(range(1, 2 * (n + 1), 2))]

ans = [0] * n

def backTrack(pos, head, seen, n):
    if pos == n: return True
    
    for arr in arrays:
        x = arr[pos]
        if x in seen: continue
        
        seenNow = seen.copy()
        nextHead = set()
        nextHead.add(x)
        seenNow.add(x)
        
        for val in head:
            if val + x in seenNow:
                break
            
            nextHead.add(val + x)
            seenNow.add(val + x)
        
        else:
            if backTrack(pos + 1, nextHead, seenNow, n):
                ans[pos] = arr[pos]
                return True
                
    return False

         
backTrack(0, set(), set(), n)    
            
print(*ans)