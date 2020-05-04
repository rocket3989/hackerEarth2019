N = int(input())

if N == 3:
    print("* . .\n. . *\n. . .")
    exit()


mat = [['.' for i in range(N)] for j in range(N)]

for i in range(N // 2):
    mat[i][2 * i] = '*'
    
for i in range(N // 2):
    if i + N // 2 == N - 1: break
    mat[1 + i + N // 2][1 + 2 * i] = '*'  
    
for row in mat:
    print(*row)