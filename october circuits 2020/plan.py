intervals = []
for f in range(int(input())):
    curr = [int(x) for x in input().split()]
    for a, b in zip(curr[1::2], curr[2::2]):
        intervals.append((a, 0))
        intervals.append((b + 1, 1))
        
        
count = 0
for pos, kind in sorted(intervals):
    
    if kind:
        count -= 1
        if count == 0:
            print(pos)
            break
    
    else:
        if count = 0 and pos != 1:
            print(1)
            break
        count += 1
    x
    