for tc in range(int(input())):
    X, Y = [int(x) for x in input().split()]
    
    if Y > X:
        print(-1)
    else:
        print(X)