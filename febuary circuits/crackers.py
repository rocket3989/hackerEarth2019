n = int(input())
vals = [int(x) for x in input().split()]
 
seen = set()
 
for i in range(1 << n):
    sumOf = 0
    for j in range(n):
        if 1 << j & i:
            sumOf += vals[j]
    if sumOf % 2 == 0:
        seen.add(sumOf)
        
print(len(seen) - 1)