import sys, resource
sys.setrecursionlimit(1000000)
resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))

N = int(input())
adj = [[] for i in range(N + 1)]
for i in range(N - 1):
    u, v = [int(x) for x in input().split()]
    adj[u].append(v)
    adj[v].append(u)
    
visited = [False] * (N + 1)

blocked = [0] + [int(x) for x in input().split()]

def dfs(node, parent):
    
    bestScore = 0
    currSize = 1
    
    for other in adj[node]:
        if other == parent: continue
        ret = dfs(other, node)
        bestScore = max(bestScore, ret[1])
        currSize += ret[0]

    if N > 1000:
        bestScore = max(bestScore, currSize)
    
    if blocked[node]:
        return (1, max(bestScore, 1))

    return (currSize, bestScore)
print(dfs(1, 0)[1])
