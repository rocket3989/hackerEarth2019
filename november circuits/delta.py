N = int(input())
lead = [(i * i) - 1 for i in range(N + 1)]
sumOver = ((N * (N+1)) // 2) ** 2
for i in range(2, N + 1):
    div = N // i 
    sumOver -= lead[i] * (((div * (div+1)) // 2) ** 2)
    for val in range(1, N // i):
        lead[(val + 1) * i] -= (val + 1) * (val + 1) * lead[i]
print(sumOver % (10**9 + 7))
