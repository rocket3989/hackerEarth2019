from collections import deque

def dfsNumber(node, parent = 0):
    count = 0
    for edge in adj[node]:
        
        if edge[0] == parent: continue
        countOf = dfsNumber(edge[0], node)
        edgeCount[edge[2]] = countOf if edge[3] == 1 else N - countOf
        count += countOf

    return count + 1

edgeCount = []
adj = []

for tc in range(int(input())):
    N, K = [int(x) for x in input().split()]
    adj = [[] for i in range(N + 1)]
    edgeCount = [0 for i in range(N - 1)]

    for edge in range(N - 1):
        x, y, a, b = [int(x) for x in input().split()]
        adj[x].append((y, a, edge, 1, b))
        adj[y].append((x, b, edge, -1, a))

    count1 = dfsNumber(1)
    # print(edgeCount)

    minCost = float('inf')
    for node in range(1, N + 1):
        costs = []
        bfs = deque()
        bfs.append((node,0))
        while(len(bfs)):
            curr, parent = bfs.popleft()
            # print(curr, parent)
            for edge in adj[curr]:
                if edge[0] == parent: continue
                # print(edge)
                if edge[3] == 1:
                    costs.append(edgeCount[edge[2]] * edge[4])
                else:
                    costs.append((N - edgeCount[edge[2]]) * edge[4])
                bfs.append((edge[0], curr))
        print(node, costs)
        minCost = min(sum(sorted(costs)[:-K or None]), minCost)
    print(minCost)




"""
1
5 1
1 2 1 1
2 3 1 1
3 4 1 1
4 5 1 1


1
4 1
1 2 1 1
2 3 1 1
2 4 1 1
"""