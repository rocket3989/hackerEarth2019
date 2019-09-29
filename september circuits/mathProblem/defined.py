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

dOccur = {}
dBene = {}

def f(p, q, n):
    ans = 0
    for i in range(1, n + 1):
        valsD = []
        ansNow = ans

        for m in range(p, q + 1):
            if m not in primes:
                continue
            for d in range(1, m*i + 1):
                if (m * i) % d != 0:
                    continue
                if ftemp(d) == 0:
                    continue

                valsD.append(d * ftemp(d))
                dOccur.setdefault(d,0)
                dOccur[d] += 1

                val = ftemp(d) / d

                dBene.setdefault(d,0)
                if i % 2 == 1:
                    ans -= val * m * i * (n // i)
                    dBene[d] -= val * m * i * (n // i)
                else:
                    ans += val * m * i * (n // i)
                    dBene[d] += val * m * i * (n // i)

        print(i, end = ' ')
        print( abs(int(ans - ansNow)), " = ", valsD )

    return int(ans)

for i in range(int(input())):
    p, q, n = [int(x) for x in input().split()]

    print(f(p, q, n)) #% (10 ** 9 + 7))
    print(dOccur)
    print(dBene)







