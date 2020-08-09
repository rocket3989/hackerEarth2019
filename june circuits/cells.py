import sys, resource
sys.setrecursionlimit(1000000)
resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))

N, M  = [int(x) for x in input().split()]

dp = [[0 for i in range(M)] for j in range(N)]

dp[0][0] = 1

arr = [[0 for i in range(M)] for j in range(N)]
dp2 = [[0 for i in range(M)] for j in range(N)]


for i in range(N):
    for j, el in enumerate(input().strip()):
        if el == '#': continue
        arr[i][j] = 1
        if i != 0: 
            dp[i][j] += dp[i - 1][j]
        if j != 0:
            dp[i][j] += dp[i][j - 1]
        
dp2[-1][-1] = arr[-1][-1]

for i in range(N - 1, -1, -1):
    for j in range(M - 1, -1, -1):
        if arr[i][j] == 0: continue
        if i != N - 1: 
            dp2[i][j] += dp2[i + 1][j]
        if j != M - 1:
            dp2[i][j] += dp2[i][j + 1]


paths = dp[0][0] + dp2[0][0]

visited, tin, low = [False for i in range(N * M)], [-1 for i in range(N * M)], [-1 for i in range(N * M)]
timer = 0

cuts = set()
def dfs(i, j, N, M):
    node = i * M + j
    visited[node] = True
    global timer
    tin[node] = timer
    low[node] = timer
    timer += 1
    
    for dj, di in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        I, J = di + i, dj + j
        if I == N or J == M or I < 0 or M < 0: continue
        if dp[I][J] == 0 or dp2[I][J] == 0: continue
        child = I * M + J
        
        if visited[child]:
            low[node] = min(low[node], tin[child])
        
        else:
            dfs(I, J, N, M)
            low[node] = min(low[node], low[child])
            if low[child] >= tin[node]:
                cuts.add((i, j))
                
                
                
                
dfs(0, 0, N, M)
cuts.add((N - 1, M - 1))



for i, (row1, row2, row3) in enumerate(zip(dp, dp2, arr)):
    row = []
    for j, (el1, el2, val) in enumerate(zip(row1, row2, row3)):
        if val:
            if paths <= 1:
                row.append(0) 
            elif (i, j) in cuts and dp[i][j] and dp2[i][j]:
                row.append(0)
            else:
                row.append(1)

        else:
            if dp[-1][-1]:
                row.append(1)
            else:
                top = 0
                
                if i != 0: 
                    top += dp[i - 1][j]
                if j != 0:
                    top += dp[i][j - 1]
                bottom = 0
                
                if i != N - 1: 
                    bottom += dp2[i + 1][j]
                if j != M - 1:
                    bottom += dp2[i][j + 1]
                    
                if bottom and top:
                    row.append(1)
                else:
                    row.append(0)
                
    
    
    print(*row)
