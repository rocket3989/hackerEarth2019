r, c, x, y = [int(x) for x in input().split()]

for i in range(r):
    for j in range(c):
        print(max(abs(i - x), abs(j - y)), end=' ')
    print()
    