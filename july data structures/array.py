N, x = [int(x) for x in input().split()]
arr = []

pre = [0]
for val in [int(x) for x in input().split()]:
    if val == x:
        arr.append(1)
        pre.append(pre[-1] + 1)
    else:
        arr.append(0)
        pre.append(pre[-1])

for q in range(int(input())):
    query = [int(x) for x in input().split()]
    
    if query[0] == 1:
        l, r, k = query[1:]
        
        l -= 1
        r -= 1
        
        
        if pre[r + 1] - pre[l] < k: 
            print(-1)
            continue
        
        for i, val in enumerate(pre[l:r + 1]):
            if val - pre[l] == k:
                print(i + l)
                break
        
        
    else:
        ind, val = query[1:]
        ind -= 1
        if val == x and arr[ind] != 1:
            arr[ind] = 1
            for i in range(ind + 1, N):
                pre[i] += 1
        
        elif arr[ind] == 1 and val != x:
            arr[ind] = 0
            for i in range(ind + 1, N):
                pre[i] -= 1