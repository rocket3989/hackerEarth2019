fact = [1, 1]
MOD = 10 ** 9 + 7

for i in range(2, 10000):
    fact.append(i * fact[-1] % MOD)

def f(p, q, r):
    ans = 0
    for i in range(p + 1):
        temp = 0
        
        for j in range(1, q + 1):
        
            ta = pow(r, j, MOD)
            tb = ((ta - 1) % MOD) * pow(ta, MOD - 2, MOD) % MOD
            temp += pow(tb, i, MOD)
            
        temp2 = fact[p] * pow(fact[p-i] * fact[i] % MOD, MOD - 2, MOD) % MOD
        
        if i & 1:
            ans -= temp * temp2
        
        else:
            ans += temp * temp2
        ans %= MOD
    return ans       
            

print(f(2, 3, 2))