fact = [1, 1]
MOD = 10 ** 9 + 7

for i in range(2, 1001):
    fact.append(fact[-1] * i)
    # precompute factorial...
    
# n, m = [int(x) for x in input().split()]
from itertools import permutations

arr = [[0 for j in range(20)] for i in range(20)]

for n in range(10):
    for m in range(1, n):
        count = 0
        for perm in permutations(range(n)):
            for i, val in enumerate(perm):
                if abs(i - val) == m:
                    break
            else:
                count += 1
                    
        arr[n][m] = count
    
    
    # this is slow, just testing
for row in arr:
    print(*row)
    
    
a(n) = n*a(n-1) - (n-2)*a(n-3) - a(n-4), for n>=5