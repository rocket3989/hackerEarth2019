N, Q = [int(x) for x in input().split()]


lastEl = 0
currLen = 1
currDist = 0

distLook = {}


for i, a in enumerate([int(x) for x in input().split()]):
    if i == 0: 
        lastEl = a
        continue
    if i == 1: 
        currLen = 2
        currDist = a - lastEl
        lastEl = a        
        continue
    if (a - lastEl) != currDist:
        distLook.setdefault(currDist, [])
        distLook[currDist].append((i - currLen + 1, currLen))
        currLen = 2
        currDist = a - lastEl
        lastEl = a
        continue
    currLen += 1
    lastEl = a
distLook.setdefault(currDist, [])
distLook[currDist].append((i - currLen + 2, currLen))


for q in range(Q):
    L, R, D = [int(x) for x in input().split()]
    maxLen = 1
    
    if D not in distLook:
        print(1)
        continue

    for ele in distLook[D]:

        if ele[0] + ele[1] < L: continue
        if ele[0] > R - maxLen: break

        maxLen = max(maxLen, min(ele[1] - (L - ele[0]), ele[1], R - ele[0] + 1, 1 + (R - L)))

    print(maxLen)