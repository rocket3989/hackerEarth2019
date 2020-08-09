for tc in range(int(input())):
    N, M = [int(x) for x in input().split()]
    
    minPos = [set(), set()]
    maxPos = [set(), set()]
    minOf, maxOf = 10 ** 6, 0
    
    for row in range(N):
        for col, el in enumerate([int(x) for x in input().split()]):
            if el == maxOf:
                maxPos[0].add(row)
                maxPos[1].add(col)
            
            elif el > maxOf:
            
                maxPos = [set(), set()]
                maxPos[0].add(row)
                maxPos[1].add(col)
                maxOf = el
                
            if el == minOf:
                minPos[0].add(row)
                minPos[1].add(col)
            
            elif el < minOf:
            
                minPos = [set(), set()]
                minPos[0].add(row)
                minPos[1].add(col)
                minOf = el
                
    rowCount = N - len(maxPos[0] | minPos[0])
    colCount = M - len(maxPos[1] | minPos[1])
    
    # print(minPos, maxPos)
    print(rowCount * colCount)