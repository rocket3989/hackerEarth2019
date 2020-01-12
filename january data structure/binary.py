from collections import deque
 
for tc in range(int(input())):
    N, K = [int(x) for x in input().split()]
    A = input()
    nextLook = deque()
 
    for i, el in enumerate(A):
        if el == '1':
            nextLook.append(i)
    
    patternLen = 0
 
    while len(nextLook) > 1 and patternLen * len(nextLook) < N:
        thisLook, nextLook = nextLook, deque()
        foundOne = False
 
        patternLen += 1
        lastSeen = thisLook[-1] - N
        while len(thisLook):
            pos = thisLook.popleft()
            if pos - lastSeen < patternLen:
                lastSeen = pos
                continue
            lastSeen = pos
            if A[(pos + patternLen) % N] == '1':
                if not foundOne:
                    foundOne = True
                    nextLook = deque()
                nextLook.append(pos)
            elif not foundOne:
                nextLook.append(pos)
 
    if len(nextLook) == 0:
        print(K - 1)
        continue
    if len(nextLook) == 1: patternLen = N
    first = min(nextLook)
    print(first + (K - 1) * patternLen)