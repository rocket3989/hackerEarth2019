import sys, resource
sys.setrecursionlimit(1000000)
resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))


MOD = 10 ** 9 + 7

from math import gcd

N, M = [int(x) for x in input().split()]

adj = [[] for i in range(N + 1)]
for i in range(M):
    u, v = [int(x) for x in input().split()]
    
    adj[u].append(v)
    adj[v].append(u)
    
disc = [float('inf') for i in range(N + 1)]

low = [float('inf') for i in range(N + 1)]

visited = [False for i in range(N + 1)]

parent = [-1 for i in range(N + 1)]

children = [0 for i in range(N + 1)]

time = 0

cuts = set()

def dfs(node):
    visited[node] = True
    
    global time
    disc[node] = time
    low[node] = time
    time += 1
    children[node] = 1
    
    for other in adj[node]:
        if not visited[other]:
            parent[other] = node
            children[node] += dfs(other)
            
            low[node] = min(low[node], low[other])
            
            if low[other] > disc[node]:
                cuts.add((min(node, other), max(node, other)))
                
        elif other != parent[node]:
            low[node] = min(low[node], low[other])
    return children[node]
    

dfs(1)

size = len(cuts)

if size == 0:
    print("0 0")
elif N & 1:
    print("0 1")
else:
    aWin = 0
    for a, b in cuts:
        count = min(children[a], children[b])
        if count & 1 == 0:
            aWin += 1
    size %= MOD
    bWin = (size - aWin) % MOD
    aWin %= MOD
    
    shared = gcd(size, aWin)
    
    print((aWin / shared) * pow(size, MOD - 2, MOD) % MOD, end=' ')

    shared = gcd(size, bWin)
    
    print((bWin / shared) * pow(size, MOD - 2, MOD) % MOD)
    
