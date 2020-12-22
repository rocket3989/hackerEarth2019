n = int(input())
# n = 20
dp = [[1, -1] for i in range(n)]

arr = [int(x) for x in input().split()]

from random import randint

# arr = [randint(1, 30) for i in range(n)]

# 1 = gt

for i in range(1, n):
    for j in range(i):
        if arr[j] <= arr[i]:
            dp[i][0] = max(dp[i][0], dp[j][1] + 1)
            
        if arr[j] >= arr[i]:
        
        
            dp[i][1] = max(dp[i][1], dp[j][0] + 1)
            

best = 0

for a, b in dp:
    best = max(best, a, b)

print(dp)

for i in range(n):
    print(f'{dp[i][0]: 4}', end='')

print()
for i in range(n):
    print(f'{dp[i][1]: 4}', end='')
print()
for i in range(n):
    print(f'{arr[i]: 4}', end='')
print()

print(best)