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
        
    
for tc in range(int(input())):
    N = int(input())
    
    ans = 0
    
    for i in range(N + 1):
        ans += comb(N, i, MOD) * comb(i, N - i, MOD)
        ans %= MOD
    print(ans)
