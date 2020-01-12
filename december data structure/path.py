def dfs1(node, dest, visited):
    if node == dest:
        path = set()
        path.add(node)
        return path
    visited.add(node)
    for other in adj[node]:
        if other not in visited:
            path = dfs1(other, dest, visited)
            if path:
                path.add(node)
                return path

def dfs2(node, parent, dest, visited, path):
    count = 0
    visited.add(node)
    if node == dest: return count
    for other in adj[node]:
        if other != parent and other in path:
            count += 1
        if other not in visited:
            count += dfs2(other, node, dest, visited, path)
    return count

N, M = [int(x) for x in input().split()]
adj = {x: [] for x in range(1, N + 1)}
for i in range(M):
    u, v = [int(x) for x in input().split()]
    adj[u].append(v)
    adj[v].append(u)

for q in range(int(input())):
    u, v = [int(x) for x in input().split()]
    visited = set()
    path = dfs1(u, v, visited)
    # print(path)
    visited = set()
    count = dfs2(u, 0, v, visited, path)
    if count == len(path) - 1:
        print(count + 1)
    else: print(-1)


"""
4 4
1 2
2 3
2 4
3 4
2
1 4
1 3


"""