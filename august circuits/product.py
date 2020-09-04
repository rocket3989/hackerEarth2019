from random import shuffle
import time
start = time.time()

N, T = [int(x) for x in input().split()]

A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]





best = float('inf')
bestB = []

iterations = 0
while time.time() - start < 24.7:
    shuffle(B)
    score = 0
    
    for a, b in zip(A, B):
        score += a * b

    if abs(score - T) < best:
        bestB = B[:]
    iterations += 1

print(iterations)
print(*A)


print(*bestB)
