MOD = 999983

def ncr(n, r): 
    num = den = 1 
    for i in range(r): 
        num = (num * (n - i)) % MOD 
        den = (den * (i + 1)) % MOD
        
    return (num * pow(den, MOD - 2, MOD)) % MOD 



for tc in range(int(input())):
    x, y = [int(x) for x in input().split()]
    
    if x > y:
        print(0)
        
    else: 
        val = ncr(x + y, x) - ncr(x + y, x - 1)
        val %= MOD
        print(val) 