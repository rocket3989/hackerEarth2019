N = int(input())

from collections import defaultdict

apples = defaultdict(list)

for i in range(N):
    y, x = [int(x) for x in input().split()]
    apples[y].append((x, i))
    
out = [0 for i in range(N)]
place = 0
left = True

for k, v in sorted(apples.items()):
    if left:
        for apple, pos in sorted(v):
            out[pos] = place
            place += 1
            
    else:
        for apple, pos in reversed(sorted(v)):
            out[pos] = place
            place += 1
    
    left = not left

print(*out, sep='\n')