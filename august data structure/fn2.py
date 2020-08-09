fact = [1, 1]
MOD = 10 ** 9 + 7

for i in range(2, 10000):
    fact.append(i * fact[-1] % MOD)

def f(p, q, r):
    ans = 0
    for i in range(1, q + 1):
        temp = 0
        ta = pow(r, i, MOD) 
        tb = (ta - 1) * pow(ta, MOD - 2, MOD) % MOD
        
                
        temp = ((pow(tb, p + 1, MOD) - 1) % MOD) * pow((tb - 1) % MOD, MOD - 2, MOD) - 1 % MOD 
            
        temp2 = fact[p] * pow(fact[p-i] * fact[i] % MOD, MOD - 2, MOD)
        
        if i & 1:
            ans -= temp * temp2
        
        else:
            ans += temp * temp2
        ans %= MOD
    return ans       
            

for tc in range(int(input())):
    p, q, r = [int(x) for x in input().split()]
    print(f(p, q, r))


