N, M, K = [int(x) for x in input().split()]


adj = [[] for i in range(N + 1)]

for i in range(M):
    u, v, w = [int(x) for x in input().split()]
    
    adj[u].append((v, w))
    adj[v].append((u, w))    
        
from heapq import heappush, heappop

costs = [float('inf') for i in range(N + 1)]
costs[1] = 0

pq = [(0, 1, [0])] # cost, node, heap

while pq:
    
    cost, node, heap = heappop(pq)
    
    
    for other, weight in adj[node]:
        newHeap = heap[:]
        
        if len(heap) < K:
            heappush(newHeap, weight)
            heappush(pq, (cost, other, newHeap))     
            costs[other] = 0
            continue
        
        if min(weight, newHeap[0]) + cost >= costs[other]:
            continue
        
        heappush(newHeap, weight)
        
        newCost = cost + heappop(newHeap)
        heappush(pq, (newCost, other, newHeap))
        
        costs[other] = newCost
    
print(*costs[1:])
        