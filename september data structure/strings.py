MOD = 10 ** 9 + 7


fact = [1, 1]

for i in range(2, 10 ** 6 + 1):
    fact.append(fact[-1] * i % MOD)


for tc in range(int(input())):
    N, M = [int(x) for x in input().split()]
    
    
    ans = (N * N - 1) % MOD
    
    other = 1
    
    for i in range(2, M + 1):
        
        other *= (N + 1) * fact[M] * pow(fact[i] * fact[M - i] % MOD, MOD - 2, MOD)
        other %= MOD
        
    ans *= other
    print(other)
    ans %= MOD
    print(ans)
    