countY = 2
for tc in range(int(input())):
    N, M = [int(x) for x in input().split()]
    
    outNode = {}
    inNode = {}

    edgeSet = set()

    fail = False

    inputs = []

    for count in range(M):

        u, v = [int(x) for x in input().split()]

        inputs.append((u,v))
        if fail: continue
        
        if u == v: continue

        if (u, v) in edgeSet: 
            fail = True

        edgeSet.add((u, v))

        outNode.setdefault(v, [])
        inNode.setdefault(u, [])
        outNode.setdefault(u, [])
        inNode.setdefault(v, [])

        for outVal in outNode[v]:
            if (u, outVal) in edgeSet: 
                fail = True
            if u != outVal:
                edgeSet.add((u, outVal))
                outNode[u].append(outVal)

        for inVal in inNode[u]:
            if (inVal, v) in edgeSet: 
                fail = True
            if v != inVal:
                edgeSet.add((inVal, v))
                inNode[v].append(inVal)
        

        outNode[u].append(v)
        inNode[v].append(u)
        
        print(u, v)
        print(inNode)
        print(outNode)  
        print(sorted(edgeSet))
        print()

    # print(N, M)
    # for val in inputs:
    #     print(*val)
    print()
    print(sorted(edgeSet))
    print(inNode)
    print(outNode)
    print(N * (N-1))

    if fail: print("No")
    else:
        if (len(edgeSet) == N * (N-1)):
            print(N, M)
            for val in inputs:
                print(*val)

        else: print("No")

"""


5 8
2 4
2 1
4 2
2 3
3 2
3 3
5 2
1 5


"""