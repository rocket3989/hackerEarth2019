from random import randint

A = [randint(0,10)]
for i in range(9):
    A.append(A[-1] + randint(0,10))
print(*A)


lastEl = 0
currLen = 1
currDist = 0

distLook = {}
for i, a in enumerate(A):
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
for i in range(11):
    if i in distLook:
        print(i, distLook[i])


for q in range(10000):
    L = randint(1, 9)
    R = randint(L, 9)
    D = randint(0, 10)

    maxLen1 = 1
    
        # print(1)
        # continue

    if D in distLook:
        for ele in distLook[D]:

            if ele[0] + ele[1] < L: continue
            if ele[0] > R - maxLen1: break

            maxLen1 = max(maxLen1, min(ele[1] - (L - ele[0]), ele[1], R - ele[0] + 1, 1 + (R - L)))

    maxLen2 = 1
    curr = 1
 
    for x1, x2 in zip(A[L - 1:R - 1], A[L:R]):
        if x2 - x1 == D:
            curr += 1
            maxLen2 = max(maxLen2, curr)
        else:
            curr = 1
    if maxLen1 != maxLen2:
        print(L, R, D, maxLen1, maxLen2)

"""
8 11 21 26 32 42 48 53 55 57

3 9 2
0 9 2




"""