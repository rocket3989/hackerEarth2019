from math import sqrt

N, M = [int(x) for x in input().split()]

arr = [int(x) for x in input().split()]

counts = [0] + [int(x) for x in input().split()]


div = int(sqrt(N))
div = 10000

curr = [0] * (M + 1)

pre = []

for i, val in enumerate(arr):
    if i % div == 0:
        pre.append(curr[:])
    curr[val] += 1


for q in range(int(input())):
    l, r = [int(x) for x in input().split()]
    l -= 1
    r -= 1
    rPos, lPos = r // div, l // div
    
    right = pre[rPos][:]
    left = pre[lPos][:]
    
    for i in range(rPos * div, r + 1):
        right[arr[i]] += 1
    
    for i in range(lPos * div, l):
        left[arr[i]] += 1
    
    
    for i, (a, b, c) in enumerate(zip(right, left, counts)):
        if i == 0: continue
        if a - b == 0: continue
        if a - b != c:
            print(0)
            break
         
    else:
        print(1)

    
    
    