N, K = [int(x) for x in input().split()]
            
arr = []

for i in range(N):  
    arr.append(int(input()))

from heapq import heappush, heappop


l = 0

minOf, maxOf = arr[0], arr[0]

mins = [(arr[0], 0)]
maxs = [(-arr[0], 0)]

count = N

for r, val in enumerate(arr):
    if r == 0: continue
    
    heappush(mins, (val, r))
    heappush(maxs, (-val, r))
    
    oldL = l
    
    while val > K + mins[0][0]:
        garb, bound = heappop(mins)
        l = max(l, bound + 1)
    
    while val + K < -maxs[0][0]:
        garb, bound = heappop(maxs)
        l = max(l, bound + 1)
    
    
    count += r - l
    
    
print(count)
    
