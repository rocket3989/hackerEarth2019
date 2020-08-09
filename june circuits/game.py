import math
MOD = 10 ** 9 + 7
N = int(input())

arr = [int(x) for x in input().split()]

counts = [0 for i in range(101)]

xorSum = 0
for val in arr:
    counts[val] += 1
    xorSum ^= val

pos = 0

for val in counts:
    if val != 0:
        counts[pos] = val
        pos += 1


N = pos

M = (1 << int(math.log2(max(counts)) + 1)) - 1

dp = [[0 for i in range(M + 1)] for j in range(N + 1)]

dp[0][0] = 1
for i in range(1, N + 1):
    for j in range(M + 1):
        dp[i][j] = (dp[i - 1][j] + dp[i - 1][j ^ counts[i - 1]]) % MOD

    
print(dp[N][xorSum])