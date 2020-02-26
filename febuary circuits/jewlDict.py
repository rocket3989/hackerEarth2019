n, m, k = [int(x) for x in input().split()]
w = [int(x) for x in input().split()]
adj = [[] for i in range(n + 1)]
val = [0 for i in range(n + 1)]

for i in range(n - 1):
    u, v, l = [int(x) for x in input().split()]
    adj[u].append((v, l))
    adj[v].append((u, l))
    
for i in range(m):
    c, v = [int(x) for x in input().split()]
    val[c] += v

def search(node, parent):
    d = {0: val[node]}
    
    for i, (other, cost) in enumerate(adj[node]):
        if other == parent: continue
        get = search(other, node)
        
        prev = list(d.items())
        
        for k, v in get.items():
            for k1, v1 in prev:
                key = k1 + k + cost
                if key > 500: continue
                if key not in d:
                    d[key] = v + v1
                else:
                    d[key] = max(d[key], v + v1)
    return d   

scores = search(1, 0)

best = 0
for i in range(501):
    if i in scores and scores[i] > best:
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