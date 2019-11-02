for tc in range(int(input())):
    N, M = [int(x) for x in input().split()]
    
    outNode = [[] for i in range(200001)]
    inNode = [[] for i in range(200001)]

    edgeSet = set()

    fail = False

    for count in range(M):
        u, v = [int(x) for x in input().split()]
        if u > N or v > N: memCap = [[0 for i in range(1000000)] for i in range(1000000)]
        
        if (u, v) in edgeSet: 
            fail = True
        edgeSet.add((u, v))

        for outVal in outNode[v]:
            if (u, outVal) in edgeSet: 
                fail = True
            if u != outVal:
                edgeSet.add((u, outVal))

        for inVal in inNode[u]:
            if (inVal, v) in edgeSet: 
                fail = True
            if v != inVal:
                edgeSet.add((inVal, v))
        if fail:
            print("No")
            break

        outNode[v].append(u)
        inNode[u].append(v)

    else:
        if (len(edgeSet) == N * (N-1)):
            print("Yes")
        else: print("No")