for tc in range(int(input())):
    N = int(input())
    arr = [0] + [int(x) for x in input().split()]
    best = [-1 for i in range(N + 1)]
    
    for i in range(1, N + 1):
        # print('i = ', i)
        unset = []
        maxSet = 0
        for bit in range(18):
            if 1 << bit & i:
                maxSet = bit
            else:
                unset.append(bit)
        
        unset = [x for x in unset if x < maxSet]
        
        # print(unset)
        val = 1 << maxSet + 1
        
        while val <= N:
            for j in range(1 << len(unset)):
                val2 = val
                for k, bit in enumerate(unset):
                    if j & (k + 1): val2 |= 1 << bit
                
                if val2 <= N:
                    best[val2] = max(best[val2], arr[i])
                    best[i] = max(best[i], arr[val2])
                    
            val += 1 << maxSet + 1
                
    
    
    
    
    
    
    
    
    for q in range(int(input())):
        k = int(input())
        
        if best[k] != -1:
            print(best[k] + arr[k])
        else:
            print(-1)
        