maxn = 10 ** 6 + 1

primes = [True] * maxn
prefix = [0, 0]

for p in range(2, maxn):
    if primes[p]:
        for i in range(2*p, maxn, p):
            primes[i] = False
        prefix.append(prefix[-1] + 1)
    else:
        prefix.append(prefix[-1])
        
for tc in range(int(input())):
    print(prefix[int(input())])