N, K = [int(x) for x in input().split()]
            
arr = []
maxes = [0]

for i in range(N):  
    arr.append(int(input()))
    maxes.append(max(maxes[-1], arr[-1]))

count = 0

maxes = maxes[1:]

for start in range(N):
    
    l, r = start, N - 1
    
    while l != r:
    
        mid = (l + r + 1) // 2
    
        if maxes[mid] - arr[start] <= K:
            l = mid
            
        else:
            r = mid - 1
    
    count += l - start + 1
    
print(count)