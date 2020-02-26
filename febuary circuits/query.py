from random import randint
from time import time
start = time()
from collections import deque
D = deque()
Q = int(input())
moves = []
for q in range(Q):
    move = tuple(int(x) for x in input().split())
    moves.append((move, q + 1))
    # if randint(0, 1):
    #     D.append((move, q + 1))
    # else:
    #     D.appendleft((move, q + 1))
 
moves.sort()
for move in moves:
    D.append(move)
 
 
 
 
curr = (0, 0, 0, 0)
out = []
 
 
for i in range(Q):
    if time() - start > 14.7:
        while len(D):
            out.append(D.popleft()[1])
        break
    bestMove = -1
    best = float('inf')
    val = 3000 // (time() - start)
    val = int(val)
    for j in range(min(val, len(D))):
        test = D.popleft()
        dist = 0
        for pair in zip(curr, test[0]):
            dist += abs(pair[0] - pair[1])
        if dist < best:
            if bestMove != -1:
                D.append(bestMove)
            bestMove = test
            best = dist
            if dist < (time() - start) * 2: break
        else:
            D.append(test)
    curr = bestMove[0]
    out.append(bestMove[1])
 
print(*out)