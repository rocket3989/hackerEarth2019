def knapsack_01_exact_min(weights, values, W):
    # 0-1 knapsack, exact total weight W, minimizing total value
    n = len(weights)
    values = [0] + values
    weights = [0] + weights
    K = [[0 for i in range(W+1)] for j in range(n+1)]
    choice = [[0 for i in range(W+1)] for j in range(n+1)]
    
    for i in range(1, n+1):
        for w in range(1, W+1):
            K[i][w] = K[i-1][w]
            choice[i][w] = '|'
            if w >= weights[i]:
                t = K[i-1][w-weights[i]]
                if (w==weights[i] or t) and (K[i][w]==0 or t+values[i] < K[i][w]):
                    choice[i][w] = '\\'
                    K[i][w] = t+values[i]
    return K[n][W], choice





for tc in range(int(input())):
    n = int(input())
    
    arr = [int(x) for x in input().split()]
    w = [abs(x) for x in arr]
    c = [1 if x < 0 else 0 for x in arr]
    
    W = sum(w)
    
    # a, b = knapsack_01_exact_min(w, c, W // 2)
    
    # print(a, b)
    
    
    # c = [1 if x > 0 else 0 for x in arr]

    # a, b = knapsack_01_exact_min(w, c, W // 2)
    
    # print(a, b)
    
    ans = -1
    
    f = [0] * W
    g = [False] * W
    g[0] = True
    
    for i in range(n):
        for j in range(W // 2):
            if g[j]:
                g[j + w[i]] = True
                
                if f[j + w[i]] == 0 or f[j + w[i]]>f[j] + c[i]:
                    f[j + w[i]] = f[j] + c[i]
    
    if g[W // 2]:
        ans = f[W // 2]
        
        
    c = [1 if x > 0 else 0 for x in arr]
    
    f = [0] * W
    g = [False] * W
    g[0] = True
    
    for i in range(n):
        for j in range(W // 2):
            if g[j]:
                g[j + w[i]] = True
                
                if f[j + w[i]] == 0 or f[j + w[i]]>f[j] + c[i]:
                    f[j + w[i]] = f[j] + c[i]
    
    if g[W // 2]:
        ans += f[W // 2]
        
    print(ans)
        
        