N = int(input())
level = 19
adj = [[] for i in range(N + 1)]
costs = [0 for i in range(N + 1)]
depth = [0 for i in range(N + 1)]
parent = [[-1 for i in range(level)] for j in range(N + 1)]

def dfs(curr, prev, cost):
    costs[curr] = cost
    depth[curr] = depth[prev] + 1
    parent[curr][0] = prev
    for child, costOf in adj[curr]:
        if child == prev: continue
        dfs(child, curr, cost + costOf)

def preComp():
    for i in range(1, level):
        for node in range(1, N + 1):
            if parent[node][i-1] == -1: continue
            parent[node][i] = parent[parent[node][i-1]][i-1]; 

def lca(u, v):
    if depth[u] > depth[v]:
        u, v = v, u
    
    diff = depth[v] - depth[u]

    for i in range(level):
        if (diff >> i ) & 1:
            v = parent[v][i]
    
    if u == v:
        return u
    
    for i in range(level - 1, -1, -1):
        if parent[u][i] != parent[v][i]:
            u = parent[u][i]
            v = parent[v][i]
    return parent[u][0]


for i in range(N - 1):
    u, v, w = [int(x) for x in input().split()]

    adj[u].append((v, w))
    adj[v].append((u, w))

dfs(1, 0, 0)

preComp()

for q in range(int(input())):
    A, B = [int(x) for x in input().split()]

    cost = costs[A] + costs[B] - 2*costs[lca(A, B)]
    print(cost)

