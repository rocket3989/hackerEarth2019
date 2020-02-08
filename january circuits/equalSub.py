N = int(input())
K = int(input())
A = [int(x) for x in input().split()]

maxOf = A[0]
l, r = 0, 1
sumEl = A[0]
maxLen = 1

while r < N + 1:
    if sumEl + K < maxOf * (r - l):
        sumEl -= A[l]
        if A[l] == maxOf:
            maxOf = max(A[l + 1:r])
        l += 1
        continue 
    maxLen = max(maxLen, r - l)
    if r == N: break
    maxOf = max(maxOf, A[r])
    sumEl += A[r]
    r += 1

print(maxLen)