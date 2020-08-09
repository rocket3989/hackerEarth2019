from collections import defaultdict 

MAX = 1000001

smallestFactor = [0 for i in range(MAX)] 


smallestFactor[0], smallestFactor[1] = 1, 1

for i in range(2, MAX): 
    if smallestFactor[i] == 0: 
        for j in range(i * 2, MAX, i): 
            if smallestFactor[j] == 0: 
                smallestFactor[j] = i 
        smallestFactor[i] = i
             
for tc in range(int(input())):
    N, M, K = [int(x) for x in input().split()]

    arr = [int(x) for x in input().split()]

    maxFactor = defaultdict(int)
    seen = set()

    for val in arr:
        if val in seen: continue
        seen.add(val)

        factors = defaultdict(int)
        
        while val > 1:
            factor = smallestFactor[val]
            
            val //= factor
            factors[factor] += 1
        
        for k, v in factors.items():
            maxFactor[k] = max(v, maxFactor[k])
        
    
    ans = 1
    for prime, count in maxFactor.items():
        ans *= pow(prime, count * K, M)
        ans %= M

    print(ans)
