for tc in range(int(input())):
    N = int(input())

    seenOnce = set()
    inPath = set()

    for i in range(N - 1):
        x, y = [int(x) for x in input().split()]

        if x not in seenOnce:
            seenOnce.add(x)
        else:
            inPath.add(x)
        
        if y not in seenOnce:
            seenOnce.add(y)
        else:
            inPath.add(y)
    
    count = 0

    for i, val in enumerate([int(x) for x in input().split()]):
        if (i + 1) in inPath:
            if val != 0: count += 1
    
    print(count)