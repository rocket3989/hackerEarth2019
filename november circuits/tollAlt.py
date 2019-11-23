from collections import deque
from random import randint
import sys
sys.setrecursionlimit(10**6)

def sumNthSmall(arr, l, r, n):
    if n > r: return sum(arr)
    pos = randint(l,r)
    pivot = arr[pos]
    arr[r], arr[pos] = arr[pos], arr[r]
    pos = l
    for i in range(l, r):
        if arr[i] <= pivot:
            arr[pos], arr[i] = arr[i], arr[pos]
            pos += 1
    arr[pos], arr[r] = arr[r], arr[pos]
    if pos == n:
        return sum(arr[:pos])
    if pos > n:
        return sumNthSmall(arr, l, pos - 1, n)
    return sumNthSmall(arr, pos + 1, r, n)

def dfsNumber(node, parent = 0):
    count = 0
    for edge in adj[node]:
        
        if edge[0] == parent: continue
        countOf = dfsNumber(edge[0], node)

        if edge[3] == 1:
            init[edge[2]] = countOf * edge[4]
            alt[edge[2]] = (N - countOf) * edge[1]
        else:
            init[edge[2]] = (N - countOf) * edge[1]
            alt[edge[2]] = countOf * edge[4]

        count += countOf

    return count + 1

minCost = 0

def dfsScore(node, parent, arr):

    global minCost
    minCost = min(sumNthSmall(arr, 0, N - 2, N - K - 1), minCost)
    for edge in adj[node]:
        if edge[0] == parent: continue
        arr[edge[2]] = alt[edge[2]]
        dfsScore(edge[0], node, arr)
        arr[edge[2]] = init[edge[2]]


init = []
alt = []
adj = []

for tc in range(int(input())):
    N, K = [int(x) for x in input().split()]
    adj = [[] for i in range(N + 1)]
    init = [0 for i in range(N - 1)]
    alt = [0 for i in range(N - 1)]

    for edge in range(N - 1):
        x, y, a, b = [int(x) for x in input().split()]
        adj[x].append((y, a, edge, 1, b))
        adj[y].append((x, b, edge, -1, a))

    count1 = dfsNumber(1)
    # print(edgeCount)

    minCost = float('inf')
    dfsScore(1, 0, init[:])
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