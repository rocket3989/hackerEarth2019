N, M = [int(x) for x in input().split()]

arr = [int(x) for x in input().split()]

counts = [0] + [int(x) for x in input().split()]

from collections import defaultdict


for q in range(int(input())):
    l, r = [int(x) for x in input().split()]
    
    count = defaultdict(int)
    
    for val in arr[l - 1:r]:
        count[val] += 1
        
    for k, v in count.items():
        if v != counts[k]:
            print(0)
            break
    else:
        print(1)