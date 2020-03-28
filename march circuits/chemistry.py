from math import gcd
def lcm(a, b):
    return a * b // gcd(a, b)


x, y, p, q = [int(x) for x in input().split()]

a = lcm(x, p)

coff = a // p

test = coff * q

b = lcm(test, y)

coff = b // q

print(coff * p // x, b // y, coff )