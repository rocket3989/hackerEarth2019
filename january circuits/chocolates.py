for tc in range(int(input())): 
    C, N = [int(x) for x in input().split()]
    if C - ((N * (N + 1)) // 2) < 0: print(C)
    else: print((C - ((N * (N + 1)) // 2)) % N)