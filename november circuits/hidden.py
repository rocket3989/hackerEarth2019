def gcd(a, b):
    if a * b == 0: return 2 if a != 1 and b != 1 else 1
    
    while b:
        b, a = a % b, b
    return a

N = int(input())

bestDist = float('inf')
bestStart = (0,0)
starts = []

for i in range(10000):
    if bestDist < i * i:
        break
    if i % 100 == 0: print(i)
    for j in range(i + 1):
        if gcd(i, j) != 1 and i * j < bestDist:
            for val in range(N * N):
                if gcd(i + (val // N), j + (val % N)) == 1: break
            else: 
                bestDist = i * j
                bestStart = (i, j)
                starts.append((i, j))

print(*bestStart, sep=', ')

print(*starts)