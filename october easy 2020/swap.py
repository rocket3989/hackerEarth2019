n = int(input())

arr = list(enumerate([int(x) for x in input().split()], 1))

norm = 0
for i, val in arr:
    norm += abs(i - val)
    
best = norm

for i in range(n):
    for j in range(i + 1, n):
        curr = norm
        curr -= abs(arr[i][0] - arr[i][1])
        curr -= abs(arr[j][0] - arr[j][1])
        
        curr += abs(arr[i][0] - arr[j][1])
        curr += abs(arr[j][0] - arr[i][1])
        best = max(best, curr)
        
print(best)