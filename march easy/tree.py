n, q = [int(x) for x in input.split()]

adj = [[] for i in range(n + 1)]

for i in range(n - 1):
    a, b = [int(x) for x in input().split()]
    
    adj[a].append(b)

typeOf = [1 for i in range(n + 1)]
parent = [0 for i in range(n + 1)]

from collections import deque
    
q = deque()

q.append((1, 1))
while q:
    node, par = 

def dfs(node):
    if typeOf[node] == 0: continue
    
    count = 1
    
    for other in adj[node]:
        count += dfs(other)
    return count

for i in range(q):
    t, v = [int(x) for x in input().split()]
    
    if t == 1:
        typeOf[v] ^= 1
    else:
        print(dfs(v))