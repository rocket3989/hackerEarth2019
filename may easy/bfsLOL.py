r, c, y, x = [int(x) for x in input().split()]
 
 
arr = [[-1 for i in range(c)] for j in range(r)]
 
 
from collections import deque
 
q = deque()
 
visited = set()
 
q.append((0, x, y))
 
visited.add((x, y))
 
while q:
    val, x, y = q.popleft()
    
    arr[y][x] = val
    
    for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]:
        X = dx + x
        Y = dy + y
        if 0 <= X < c and 0 <= Y < r:
            if (X, Y) in visited: continue
            
            q.append((val + 1, X, Y))
            visited.add((X, Y))
            
for row in arr:
    print(*row)