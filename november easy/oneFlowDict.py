for tc in range(int(input())):
    N, M = [int(x) for x in input().split()]
    
    outNode = {}
    inNode = {}

    edgeSet = set()

    fail = False

    if M < N: print("No")

    else:
        for count in range(M):

            u, v = [int(x) for x in input().split()]
            
            if u == v: continue

            if (u, v) in edgeSet: 
                fail = True
                
            edgeSet.add((u, v))

            outNode.setdefault(v, [])
            inNode.setdefault(u, [])

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
            
            outNode.setdefault(u, [])
            inNode.setdefault(v, [])

            outNode[u].append(v)
            inNode[v].append(u)

        else:
            if (len(edgeSet) == N * (N-1)):
                print("Yes")
            else: print("No")