n, k = [int(x) for x in input().split()]

adj = [[] for i in range(n + 1)]
pathCount = [0 for i in range(k)]

for i in range(2, n + 1):
    p, c = [int(x) for x in input().split()]
    adj[i].append((p, c))
    adj[p].append((i, c))

def dfs(node, parent, colors):
    
    count = 0
    for color in colors:
        if color: count += 1
    pathCount[count] += 1

    for other in adj[node]:
        dest, color = other
        if dest == parent: continue
        colors[color] += 1
        dfs(dest, node, colors)
        colors[color] -= 1

for node in range(1, n + 1):
    dfs(node, -1, [0 for i in range(k)])
    
print(*pathCount)