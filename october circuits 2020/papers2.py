N, M = [int(x) for x in input().split()]
N += 1

adj = [[] for i in range(N)] 
cycles = [[] for i in range(N)] 

h = [float('inf') for i in range(N)]
d = [float('inf') for i in range(N)]
p = [-1 for i in range(N)]
c = [0 for i in range(N)]

  
for i in range(M):
    u, v, cost = [int(x) for x in input().split()]
    
    adj[u].append((v, cost, i))
    adj[v].append((u, cost, i))
    

h[1] = 0

cuts = set()
totalCost = 0

def dfs(v):
    d[v] = h[v]
    c[v] = 1
    for u, cost, i in adj[v]:
    
        if c[u] == 0:
            p[u] = v
            dfs(u)
            d[v] = min(d[v], d[u])
            
            if d[u] > h[v]:
                cuts.add(i)
                global totalCost
                totalCost ^= cost
        
        elif u != p[v]:
            d[v] = min(d[v], h[u])
            
    c[v] = 2
    
dfs(1)

if totalCost:
    print("YES")
    
else:
    print("NO")