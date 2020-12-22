n = int(input())

inarr = [int(x) for x in input().split()]
from collections import defaultdict
from math import log2

ans = 0

seen = defaultdict(int)

arr = []
for val in inarr:
    if seen[val] < 2:
        arr.append(val)
        seen[val] += 1

while len(arr) > 1:
    bins = defaultdict(list)
    
    for val in arr:
        bins[int(log2(val))].append(val)
        
    for pos, lis in sorted(bins.items(), reverse=True):
        if len(lis) < 2: continue
        curr = 1 << pos
        arr = []
        ans += curr
        for val in lis:
            if val ^ curr:
                arr.append(val ^ curr)
        break
print(ans)
