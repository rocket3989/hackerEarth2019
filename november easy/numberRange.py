
def ncr(n, r, p): 

    num = den = 1 
    for i in range(r): 
        num = (num * (n - i)) % p 
        den = (den * (i + 1)) % p 
    return (num * pow(den, p - 2, p)) % p 

l, r, n = [int(x) for x in input().split()]

sumRange = 0
for val in [int(x) for x in input().split()]:
    sumRange += val if val > 0 else 1

if(r - l < sumRange):
    print(0)
else:
    print(ncr(n + (r - l - sumRange), n, 10 ** 9 + 7))