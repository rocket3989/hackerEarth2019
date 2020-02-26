from heapq import heappop, heappush
from collections import deque
 
N, Q = [int(x) for x in input().split()]
 
adj = [[] for i in range(N + 1)]
for edge in range(N - 1):
    u, v = [int(x) for x in input().split()]
    adj[u].append(v)
    adj[v].append(u)
ll = max(len(a) for a in adj) == 2
 
visited = [False for i in range(N + 1)]
visited[1] = True
 
q = deque()
q.append(1)
last = -1
while len(q):
    node = q.popleft()
    for other in adj[node]:
        if visited[other]: continue
        visited[other] = True
        q.append(other)
    last = node
 
parentOf = [-1 for i in range(N + 1)]
parentOf[last] = 0
 
q = deque()
q.append((last, 0))
 
while len(q):
    node, dist = q.popleft()
    for other in adj[node]:
        if parentOf[other] != -1: continue
        parentOf[other] = node
        q.append((other, dist + 1))
    root = node
    diameter = dist
 
for i in range(diameter // 2):
    root = parentOf[root]
 
 
 
# def dfs(node, parent, depth):
 
#     deepest = node
#     maxDepth = depth
    
#     for other in adj[node]:
#         if other == parent: continue
#         test, deep = dfs(other, node, depth + 1)
#         if test > maxDepth:
#             maxDepth = test
#             deepest = deep
    
#     if maxDepth == depth * 2:
#         deepest = node
        
#     return (maxDepth, deepest)        
 
 
# diameter, root = dfs(last, -1, 0)
 
# root = 1
 
if ll:
    for i in range(1, N + 1):
        if len(adj[i]) == 1:
            root = i
            break
 
 
 
 
 
fromRoot = [-1 for i in range(N + 1)]
parentOf = [-1 for i in range(N + 1)]
parentOf[root] = 0
fromRoot[root] = 0
 
    
q = deque()
q.append((root, 0))
 
while len(q):
    node, dist = q.popleft()
    fromRoot[node] = dist
    for other in adj[node]:
        if parentOf[other] != -1: continue
        parentOf[other] = node
        q.append((other, dist + 1))
       
if ll:
    for q in range(Q):
        n = int(input())
        arr = [fromRoot[int(x)] for x in input().split()] 
        s1 = min(arr)
        s2 = max(arr)
        
        print((s2 - s1 + 1) // 2)
    exit()
    
        
        
        
        
 
for q in range(Q):
    dist = [-1 for i in range(N + 1)]
    dist[0] = 0
    
    n = int(input())
    arr = [int(x) for x in input().split()]
    
    lost = set(arr)
    
    if len(arr) == 1: 
        print(0)
        continue
        
    h = []
    
    for el in arr:
        heappush(h, (-fromRoot[el], el))
        dist[el] = 1
        
    # print(lost)
    
    # TEST LEN H for SINGLE PARENT// then done, that is root for dfs
    while len(h) > 1:
        rootDist, node = heappop(h)
        if dist[parentOf[node]] == -1:
            heappush(h, (rootDist + 1, parentOf[node]))
            dist[parentOf[node]] = dist[node] + 1
        else:
            dist[parentOf[node]] = max(dist[node] + 1, dist[parentOf[node]])
    # print(h[0][1])
    
    node, parent, prev = h[0][1], 0, -1 
    
    while True:
        options = []
        if prev != -1:
            options.append((prev, -1))
            
        if node in lost:
            options.append((0, -1))
            
        for i, other in enumerate(adj[node]):
            if other == parent: continue
            if dist[other] != -1:
                options.append((dist[other], i))
        options.sort()
        
        if len(options) < 2:
            parent = node
            node = adj[node][options[0][1]]
            prev = -1
            continue
        
        if options[-1][0] - options[-2][0] <= 1:
            print(options[-1][0])
            break
    
        node, parent, prev = adj[node][options[-1][1]], node, options[-2][0] + 1