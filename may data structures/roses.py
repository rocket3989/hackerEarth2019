N = int(input())

roses  = [int(x) for x in input().split()]

last = -1

pos = (0, 0)

best = 0

for i, rose in enumerate(roses):
    if rose > last:
        last = rose
        continue
    
    if rose <= roses[i - 2]: 
        best = max(best, i - pos[0] - 1)
        pos = (i, i)
        last = rose
        continue
    
    best = max(best, i - pos[0] - 1)
    pos = pos[1], i
    last = rose
    
best = max(best, len(roses) - pos[0] - 1)

if pos == (0, 0):
    best = N

last = -1

pos = (0, 0)

for i, rose in enumerate(roses):
    if rose > last:
        last = rose
        continue
    
    
    best = max(best, i - pos[0] - 1)
    pos = pos[1], i
    last = rose
    
best = max(best, len(roses) - pos[0] - 1)
  
if pos == (0, 0):
    best = N
print(best)    
    