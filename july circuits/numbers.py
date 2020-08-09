from collections import Counter


N = int(input())

count = 0

edges = []
for i in range(N - 1):
    A, B = [int(x) for x in input().split()]
    
    edges.append((A, B))

parent = [i for i in range(N + 1)]

labels = [-1] + [int(x) for x in input().split()]

labelCount = Counter(labels)

tracked = {k for k, v in labelCount.items() if v > 1}

nodes = [Counter((labels[i],)) if labels[i] in tracked else Counter() for i in range(N + 1)]


def parOf(node):
    if node != parent[node]:
        parent[node] = parOf(parent[node])
	
    return parent[node]

output = []
for edge in reversed([int(x) for x in input().split()]):
    edge -= 1
    
    curr = 0
    A, B = edges[edge]
    x = parOf(A)
    y = parOf(B)

    delete = []

    if len(nodes[y]) > len(nodes[x]):
        x, y = y, x


    for k, v in nodes[y].items():
        if k in nodes[x]:
            curr += v * nodes[x][k]
        nodes[x][k] += v


    nodes[y] = False
    parent[y] = x
    
    output.append(curr)


print(*reversed(output), sep='\n')