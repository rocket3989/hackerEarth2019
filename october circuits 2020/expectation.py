MOD = 10 ** 9 + 7

N = int(input())

cells = N * 2

from collections import defaultdict
counts = defaultdict(int)

for i in range(1 << cells):
    grid = [[0 for x in range(N)] for y in range(2)]
    
    
    for j in range(cells):
        if (1 << j) & i:
            grid[j // N][j % N] = 1
    
    count = 0
    
    for x in range(2):
        for y in range(N):
            if grid[x][y] == -1: continue
            
            count += 1
            curr = grid[x][y]
            stack = [(x, y)]
            
            while stack:
                r, c = stack.pop()
                if grid[r][c] != curr: continue
                
                grid[r][c] = -1
                
                for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    R, C = dr + r, dc + c
                    if 0 <= R < 2 and 0 <= C < N: stack.append((R, C))
    counts[count] += 1
                
                
print(counts)

count = 0

for k, v in counts.items():
    count += k * v
    
print(count)
# print((count % MOD) * pow(pow(2, cells, MOD), MOD - 2, MOD) % MOD)