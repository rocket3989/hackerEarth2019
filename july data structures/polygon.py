N = int(input())
MOD = 10 ** 9 + 7

fact = [1, 1]
for i in range(2, 100001):
    fact.append(fact[-1] * i % MOD)
    
def comb(n, r, MOD):
    if r == 0:
        return 1
    if r > n:
        return 0
    return fact[n] * pow(fact[n - r], MOD - 2, MOD) * pow(fact[r], MOD - 2, MOD)
    
    
from collections import defaultdict

arr = [int(x) for x in input().split()]
lens = defaultdict(int)

for val in arr:
    lens[val] += 1
    
ans = 0
for k, val in lens.items():
    if val >= 3:
        ans += pow(2, val, MOD) - comb(val, 2, MOD) - val - 1
        ans %= MOD
        
print(ans)
 
