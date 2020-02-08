n, k = [int(x) for x in input().split()]

dp = [0 for i in range(n + k)]

dp[k - 1] = 1
dp[k] = 1
for i in range(k + 1, n + k):
    dp[i] = 2 * dp[i - 1] - dp[i - k - 1] 
    dp[i] %= 10 ** 9 + 7
print(dp[n + k - 2])

# https://www.geeksforgeeks.org/n-bonacci-numbers/