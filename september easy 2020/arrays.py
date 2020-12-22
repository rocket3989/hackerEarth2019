from collections import defaultdict

n, m, K = [int(x) for x in input().split()]


values = defaultdict(int)

for i in range(n):
    a, b, c = [int(x) for x in input().split()]
    values[(a % m, b % m, c % m)] += 1
    
    
l, r = [], []
    
for i in range(3):
    L, R = [int(x) for x in input().split()]
    l.append(L)
    r.append(R)

for x in range(l[0], min(l[0] + m, r[0] + 1)):
    for y in range(l[1], min(l[1] + m, r[1] + 1)):
        for z in range(l[2], min(l[2] + m, r[2] + 1)):
            
            found = 0
            
            for k, v in values.items():
                if (x * k[0] + y * k[1] - z * k[2]) % m == 0:
                    found += v
                    if found > K: break
            
            if found == K:
                print(x, y, z)
                exit()

print(-1)