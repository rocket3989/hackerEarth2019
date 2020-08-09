# import sys, resource
# sys.setrecursionlimit(1000000)
# resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))

N, M, Q = [int(x) for x in input().split()]

direction = [0] + [int(x) for x in input().split()]


clockwise = [0 for i in range(N + 1)]

adj = [[] for i in range(N + 1)]

parent = [-1 for i in range(N + 1)]

cursed = [False for i in range(N + 1)]

for i in range(M):
    u, v = [int(x) for x in input().split()]
    adj[u].append(v)
    adj[v].append(u)
    
    
def parOf(node):
    if node != parent[node]:
        parent[node] = parOf(parent[node])
	
    return parent[node]


def dfs(node):
    
    for other in adj[node]:
        if parent[other] == -1:
            parent[other] = node
            
            clockwise[other] = -1 * direction[other] * direction[node] * clockwise[node]
            dfs(other)
            continue
        
        x = parOf(node)
        y = parOf(other)
        
        
        if clockwise[node] * direction[node] == clockwise[other] * direction[other]:
            cursed[x] = True
    
        else:
            cursed[x] = cursed[x] or cursed[y]
    
        parent[y] = x    
    
    
for i in range(1, N):
    if parent[i] != -1: continue
    
    clockwise[i] = 1
    parent[i] = i
    dfs(i)

for q in range(Q):
    g1, g2, d1, d2 = [int(x) for x in input().split()]
    
    if cursed[parOf(g1)] or cursed[parOf(g2)]:
        print("NO")
        continue
    
    if parOf(g1) != parOf(g2):
        print("YES")
        continue
    
    if clockwise[g1] * d1 == clockwise[g2] * d2:
        print("YES")
    
    else:
        print("NO")
