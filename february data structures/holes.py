def intersect(rect1, rect2):
    return max(rect1[0], rect2[0]) <= min(rect1[2], rect2[2]) and max(rect1[3], rect2[3]) <= min(rect1[1], rect2[1])

def children(node):
    yield node
    for other in sub[node]:
        yield from children(other)
    
for tc in range(int(input())):
    n, W, L = [int(x) for x in input().split()]
    rects = []
    path = (0, L, W, 0)
    for i in range(n):
        rect = tuple(int(x) for x in input().split()) # x1, y1, x2, y2
        if intersect(rect, path):
            rects.append(rect)
    
    n = len(rects) - 1 
    parent = [i for i in range(n + 1)]
    sub = [[] for i in range(n + 1)]   
    
    for i, rect in enumerate(rects):
        for j, other in enumerate(rects[:i]):
            if parent[i] == parent[j]: continue
            if not intersect(rect, other): continue
        
            if parent[i] == i:
                parent[i] = parent[j]
                sub[parent[i]].append(i)
            else:
                parent[j] = parent[i]
                sub[parent[i]].append(j)
                
                
    jumps = 0   
    
    
    for i, node in enumerate(parent):
        if node != i: continue
        rBound, lBound = False, False
        
        for child in children(node):
            lBound = lBound or rects[child][0] == 0
            rBound = rBound or rects[child][2] >= W
            if rBound and lBound:
                jumps += 1
                break

    print(jumps)