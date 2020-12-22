for tc in range(int(input())):
    n, m = [int(x) for x in input().split()]
    
    mat = []
    
    for i in range(n):
        mat.append(input())
    
    best = 0
    for i in range(n):
        curr = 0
        for j in range(m):
            if mat[i][j] == '#' and (i == 0 or mat[i - 1][j] == '.'):
                curr += 1
                best = max(curr, best)
            else:
                curr = 0
        
        curr = 0
        for j in range(m):
            if mat[i][j] == '#' and (i == n - 1 or mat[i + 1][j] == '.'):
                curr += 1
                best = max(curr, best)
            else:
                curr = 0
                
        
    for i in range(m):
        curr = 0
        for j in range(n):
            if mat[j][i] == '#' and (i == 0 or mat[j][i - 1] == '.'):
                curr += 1
                best = max(curr, best)
            else:
                curr = 0
        
        curr = 0
        for j in range(n):
            if mat[j][i] == '#' and (i == m - 1 or mat[j][i + 1] == '.'):
                curr += 1
                best = max(curr, best)
            else:
                curr = 0
    
    print(best)   
        
    
                
        
        
    