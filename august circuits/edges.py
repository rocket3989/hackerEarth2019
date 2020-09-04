import sys, resource
sys.setrecursionlimit(1000000)
# resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))


N, M = [int(x) for x in input().split()]

a, b = [int(x) for x in input().split()]


adj = [[] for i in range(N + 1)]
for i in range(M):
    u, v = [int(x) for x in input().split()]
    
    adj[u].append(v)
    adj[v].append(u)
    
disc = [float('inf') for i in range(N + 1)]

low = [float('inf') for i in range(N + 1)]

visited = [False for i in range(N + 1)]

parent = [-1 for i in range(N + 1)]

time = 0

cuts = set()

def dfs(node):
    visited[node] = True
    
    global time
    disc[node] = time
    low[node] = time
    time += 1
    
    for other in adj[node]:
        if not visited[other]:
            parent[other] = node
            dfs(other)
            
            low[node] = min(low[node], low[other])
            
            if low[other] > disc[node]:
                cuts.add((min(node, other), max(node, other)))
                
        elif other != parent[node]:
            low[node] = min(low[node], low[other])
    

dfs(1)



def dfs2(node, dest, seen):
    if node == dest:
        return 0
    if node in seen:
        return -1
        
    seen.add(node)
    
    for other in adj[node]:
        ret = dfs2(other, dest, seen)
        
        if ret != - 1: 
            if (min(node, other), max(node, other)) in cuts:
                ret += 1
            return ret
    
    return -1

print(dfs2(a, b, set()))
            
        
        
