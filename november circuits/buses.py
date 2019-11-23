count = 0

def dfs(node, parent, rel):
    global count
    if node in terminals:
        count += rel
        for child in adj[node]:
            if child == parent: continue
            dfs(child, node, 0)
        return True
    found = False
    for child in adj[node]:
        if child == parent: continue
        if found: dfs(child, node, 0)
        else: found = dfs(child, node, rel + 1)
    return found

N, K = [int(x) for x in input().split()]

adj = [[] for i in range(N + 1)]

for i in range(N - 1):
    x, y = [int(x) for x in input().split()]
    adj[x].append(y)
    adj[y].append(x)

terminals = set([int(x) for x in input().split()])

dfs(next(iter(terminals)), 0, 0)
print(count + len(terminals))