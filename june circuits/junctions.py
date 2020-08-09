from collections import defaultdict

N = int(input())
adj = [[] for i in range(N + 1)]

for i in range(N - 1):
    u, v = [int(x) for x in input().split()]
    adj[u].append(v)
    adj[v].append(u)

parent = [(-1, -1) for i in range(N + 1)]

def lookup(u, v):
    return (min(u, v), max(u, v))

def dfs(node):
    
    for child in adj[node]:
        if child == parent[node][0]: continue
        parent[child] = (node, parent[node][1] + 1)
        dfs(child)
        
costs = defaultdict(int)

dfs(1)

for i in range(int(input())):
    S, D, L = [int(x) for x in input().split()]
    
    sNode, sDepth = S, parent[S][1] + 1
    dNode, dDepth = D, parent[D][1] + 1
    
    
    pathRev = []
    path = []
    
    while sNode != dNode:
        if sDepth < dDepth:
            dDepth -= 1
            pathRev.append(dNode)
            dNode = parent[dNode][0]
            
        else:
            sDepth -= 1
            path.append(sNode)
            sNode = parent[sNode][0]
    path.append(sNode)
    
    pathRev.reverse()
    
    path = path[:] + pathRev[:]
    
    cost = 1
    for a, b in zip(path, path[1:]):
        
        costs[lookup(a, b)] += min(cost, L)
        
        L -= cost
        
        cost += 1
        if L <= 0: break


def dfs2(node):
    best = 0
    for child in adj[node]:
        if child == parent[node][0]: continue
        best = max(dfs2(child) + costs[lookup(node, child)], best)
    
    return best

print(dfs2(1))
    