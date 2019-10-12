MAX = 10**6 + 6
 
phi = [i for i in range(MAX)]
primes = []
 
 
for p in range(2, MAX):
    
    if (phi[p] == p): 
        primes.append(p)
        
        phi[p] = p - 1
 
        for i in range(2 * p, MAX, p): 
            phi[i] = (phi[i] // p) * (p - 1) 
 
for tc in range(int(input())):
    N = int(input())
    
    countOut = N - phi[N]
 
    divisors = 1
 
    for p in primes:
        count = 0
        if N % p == 0:
            while N % p == 0:
                N = N // p
                count += 1
            divisors *= count + 1

    print(countOut - divisors + 1)
 
  