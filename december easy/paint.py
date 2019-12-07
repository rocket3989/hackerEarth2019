for tc in range(int(input())):
    n, m, k = [int(x) for x in input().split()]
    matrix = []
    for j in range(n):
        matrix.append([int(x) for x in input().split()])

    best = float('inf')

    # horizontal 

    if m >= k:
        for row in range(n - 1):
            curr = 0
            for i, (top, bottom) in enumerate(zip(matrix[row], matrix[row + 1])):
                curr += top + bottom
                if i >= k:
                    curr -= matrix[row][i - k] + matrix[row + 1][i - k]
                if i >= k - 1:
                    best = min(best, curr)

    if n >= k:
        for col in range(m - 1):
            curr = 0
            for i in range(n):
                curr += matrix[i][col] + matrix[i][col + 1]
                if i >= k:
                    curr -= matrix[i - k][col] + matrix[i - k][col + 1]
                if i >= k - 1:
                    best = min(best, curr)  

    if best != float('inf'):
        print(best)
    else:
        print(-1)
