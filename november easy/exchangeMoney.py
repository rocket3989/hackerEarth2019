from math import gcd

N, Q = [int(x) for x in input().split()]

denom = [int(x) for x in input().split()]

gcdInput = denom[0]

for val in denom[1:]:
    gcdInput = gcd(gcdInput, val)

for query in range(Q):
    test = int(input())
    if test % gcdInput == 0:
        print("YES")
    else: print("NO")