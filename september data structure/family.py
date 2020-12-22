N, Q = [int(x) for x in input().split()]

adj = [[] for i in range(N + 1)]

for i in range(N - 1):
    u, v = [int(x) for x in input().split()]
    
    adj[u].append(v)
    adj[v].append(u)
    
ancestors = [[-1] * 20 for i in range(N + 1)]
depths = [-1 for i in range(N + 1)]

def dfs(node, parent, depth):
    ancestors[node][0] = parent
    depths[node] = depth
    for other in adj[node]:
        if other == parent: continue
        dfs(other, node, depth + 1)


dfs(1, -1, 0)

for i in range(1, N + 1):
    for j in range(1, 20):
        ancestors[i][j] = ancestors[ancestors[i][j - 1]][j - 1]
        



for query in range(Q):
    u, k = [int(x) for x in input().split()]
    
    num = list(bin(k)[2:])
    # print(num)
    # print("DDDDDDDD", query)
    for i, val in enumerate(num):
        # print(u)
        if val == '0': continue
        
        pos = len(num) - i - 1
        
        if 1 << pos > depths[u]:
            print(-1)
            break
        u = ancestors[u][pos]
        
    else:
        print(u)        
        