for tc in range(int(input())):
    N, M = [int(x) for x in input().split()]
    
    sumOf = 0
    while N:
        sumOf += ((N // 2) + (N % 2)) ** 2
        N //= 2
        sumOf %= M
        
    print(sumOf)