n, m, k = [int(x) for x in input().split()]
w = [int(x) for x in input().split()]
adj1 = [[] for i in range(n + 1)]
adj = [[] for i in range(n + 1)]
val = [0 for i in range(n + 1)]
edge = []
dest = [0 for i in range(n)]
 
for i in range(n - 1):
    u, v, l = [int(x) for x in input().split()]
    adj1[u].append((v, i))
    adj1[v].append((u, i))
    
    edge.append(l)
    dest.append(v)
for i in range(m):
    c, v = [int(x) for x in input().split()]
    val[c] += v
 
def dfs(node, parent):
    for other, edge in adj1[node]:
        if other == parent: continue
        adj[node].append(edge)
        dest[edge] = other
        dfs(other, node)
 
dfs(1, -1)
 
# print(adj)
# print(edge)
# print(val)
# print(dest)
 
scores = [0 for i in range(501)]
 
def search(options, weight, score):
    # print(options, weight)
    if weight > 500: return
    
    scores[weight] = max(scores[weight], score)
   
    
    for i, option in enumerate(options):
        if edge[option] + weight > 500: continue
        search(options[i + 1:] + adj[dest[option]], weight + edge[option], score + val[dest[option]])
 
search(adj[1], 0, val[1])
 
best = 0
for i in range(501):
    if scores[i] > best:
        best = scores[i]
    else:
        scores[i] = best
 
print(*[scores[cost // 2] for cost in w])
 
"""
5 5 4
1 10 20 30 30
2 1 1
2 3 2
3 4 3
3 5 4
1 1
2 2
3 3
4 4
5 5
"""