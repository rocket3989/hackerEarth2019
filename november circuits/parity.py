N = int(input())
r = [0] * (N + 1)
c = [0] * (N + 1)
sumR = 0
sumC = 0
for i, val in enumerate([int(x) for x in input().split()]):
    r[i + 1] = val % 2
    sumR += r[i + 1]

for i, val in enumerate([int(x) for x in input().split()]):
    c[i + 1] = val % 2
    sumC += c[i + 1]

cChange = not (sumC == N or sumC == 0)
rChange = not (sumR == N or sumR == 0)
print(r, c)

for query in range(int(input())):
    y1, x1 = [int(x) for x in input().split()]
    y2, x2 = [int(x) for x in input().split()]

    if c[x1] ^ c[x2] ^ r[y1] ^ r[y2] == 0:
        if (rChange or all([x == c[x1] for x in c[min(x1, x2):max(x1, x2)]])) and (cChange or all([y == r[y1] for y in r[min(y1, y2):max(y1, y2)]])):
            print("YES")
        else: print("NO")
    else: print("NO")
    
"""
3
1 0 1
1 5 3
30
2 1
3 3
3 1
1 3
1 1
1 3
"""