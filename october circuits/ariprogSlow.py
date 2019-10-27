N, Q = [int(x) for x in input().split()]
 
A = [int(x) for x in input().split()]
 
for q in range(Q):
    L, R, D = [int(x) for x in input().split()]
    maxLen = 1
    curr = 1
 
    for x1, x2 in zip(A[L - 1:R - 1], A[L:R]):
        print(x1, x2)
        if x2 - x1 == D:
            curr += 1
            maxLen = max(maxLen, curr)
        else:
            curr = 1
    print(maxLen)