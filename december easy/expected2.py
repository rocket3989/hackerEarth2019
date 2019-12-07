N = int(input())
level = 19
adj = [[] for i in range(N + 1)]
costs = [0 for i in range(N + 1)]
depth = [0 for i in range(N + 1)]
parent = [[-1 for i in range(level)] for j in range(N + 1)]

def dfs(node, parent, target, cost):
    if node == target: return cost
    

    for child, weight in adj[node]:
        if child == parent: continue
        costThis = dfs(child, node, target, cost + weight) + cost
        if costThis: 
            print(node, parent, child, target)
            return costThis
    return 0




for i in range(N - 1):
    u, v, w = [int(x) for x in input().split()]

    adj[u].append((v, w))
    adj[v].append((u, w))

for i, thing in enumerate(adj):
    print(i, thing)

for q in range(int(input())):
    A, B = [int(x) for x in input().split()]

    cost = dfs(A, 0, B, 0)
    print(cost)

