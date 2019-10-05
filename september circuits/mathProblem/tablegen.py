import itertools
MAXPRIME = 10 ** 5

def psieve():
    yield from (2, 3, 5, 7)
    D = {}
    ps = psieve()
    next(ps)
    p = next(ps)
    assert p == 3
    psq = p*p
    for i in itertools.count(9, 2):
        if i in D:      # composite
            step = D.pop(i)
        elif i < psq:   # prime
            yield i
            if i > MAXPRIME:
                return
            continue
        else:           # composite, = p*p
            assert i == psq
            step = 2*p
            p = next(ps)
            psq = p*p
        i += step
        while i in D:
            i += step
        D[i] = step


primes = list(psieve())
# print(primes)

def ftemp(d):
    if d == 1:
        return 1
    temp = 0
    for prime in primes:
        if prime > d:
            break
        if d % (prime**2) == 0: return 0
        if d % prime == 0:
            temp += 1
    if temp % 2 == 0:
        return 1
    return -1


def f(p, q, n):
    ans = 0
    for i in range(1, n + 1):
        valsD = []

        for m in range(p, q + 1):
            if m not in primes:
                continue
            for d in range(1, m*i + 1):
                if (m * i) % d != 0:
                    continue
                valsD.append(d)
                val = ftemp(d) / d
                if i % 2 == 1:
                    ans -= val * m * i * (n // i)

                else:
                    ans += val * m * i * (n // i)
        

    return int(ans)

base = [int(f(173, 173, i) // (-173 + 1)) for i in range(56)]

print("  n:  ", end='')

for n in range(1, 25):
    print("{:6}".format(n), end='') 
print("\n")

print("nor:  ", end='')
for n in range(1, 25):
    print("{:6}".format(base[n]), end='') 
print("\n")
dif = []
print("dif:  ", end='')
for n in range(1, 25):
    print("{:6}".format(base[n + 1] - base[n]), end='') 
    if (n) % 4 == 3:
        dif.append(base[n + 1] - base[n])
print("\n")

for p in primes[:20]:
    print("{:3}:  ".format(p), end='') 
    error = 0
    primary = -p + 1

    for n in range(1, 25):
        val = abs(int(f(p, p, n)/primary) - base[n])
        # val = int(f(p, p, n)//primary)
        if val != error:
        # print("{:6}".format(val//primary) , end='')
            print("{:6}".format(val - error), end='') 
            error = val 
        else:
            print("      ", end='')

    print()
print(dif)
# print([dif[n + 1] - dif[n] for n in range(11)])
from fractions import gcd
def lcm(a, b):
    return abs(a*b) // gcd(a, b)


print([lcm(n, 16)//16 for n in range(1, 40)])

# 3 9 10


# for i, prime in enumerate(primes[:20]):
#     print(i + 1, ": ",prime)
# print()


# print(f(173, 173, 1000) // (-173 + 1))
# print(f(41, 41, 1000) // (-41 + 1))


