from collections import deque

def intersect(rect1, rect2):
    return max(rect1[0], rect2[0]) <= min(rect1[2], rect2[2]) and max(rect1[3], rect2[3]) <= min(rect1[1], rect2[1])


for tc in range(int(input())):
    n, W, L = [int(x) for x in input().split()]
    rects = [0]
    path = (0, L, W, 0)
    for i in range(n):
        rect = tuple(int(x) for x in input().split()) # x1, y1, x2, y2
        if intersect(rect, path):
            rects.append(rect)
    
    n = len(rects) - 1  
    parent = [i for i in range(n + 1)]
    intersects = []
    adj = [[] for i in range(n + 1)]
    
    
    for i, rect in enumerate(rects):
        if i == 0: continue
        for j, other in enumerate(rects[:i]):
            if j == 0: continue
            if intersect(rect, other):
                adj[i].append(j)
                adj[j].append(i)
    
    visited = [False for i in range(n + 1)]
    
    q = deque()
    for i in range(1, n + 1):
        if visited[i]: continue
        
        intersects.append([])
        q.append(i)
        while len(q):
            node = q.popleft()
            intersects[-1].append(rects[node])
            for other in adj[node]:
                if visited[other]: continue
                q.append(other)
            visited[node] = True
        
                    
    jumps = 0    
            
    for group in intersects:
        events = []
        relevant = False
        for rect in group:
            events.append((rect[0], 0))
            events.append((rect[2], 1))
            if rect[0] == 0: relevant = True
        if not relevant: continue
        
        count = 0
        last = 0
        for loc, event in sorted(events):
            last = loc
            if event == 0:
                count += 1
            else:
                count -= 1
            if count == 0:
                break
        if last >= W:
            jumps += 1
    print(jumps)
        
        
# {0: [(4, 2, 6, 1), (4, 6, 6, 2), (0, 7, 5, 5)], 1: [(2, 12, 4, 8), (3, 10, 5, 9)]}