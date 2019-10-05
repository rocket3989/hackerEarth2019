
from math import log10

def primes2(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * int(n // 3)
    for i in range(1,int(n**0.5)//3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      k*k//3      ::2*k] = [False] * int((n//6-k*k//6-1)//k+1)
        sieve[k*(k-2*(i&1)+4)//3::2*k] = [False] * int((n//6-k*(k-2*(i&1)+4)//6-1)//k+1)
    return set([2,3] + [3*i+1|1 for i in range(1,int(n//3-correction)) if sieve[i]])




A, B, K = [int(x) for x in input().split()]

MAXPRIME = log10(B) * 9
primes = primes2(MAXPRIME)
count = 0

for i in range((A // K) * K, B + 1, K):
    if i < A: continue
    r = 0
    while i:
        r, i = r + i % 10, i // 10
    if r in primes:
        count += 1
print(count)