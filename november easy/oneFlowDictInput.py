import sys

sys.stdin = open('in2.txt')  

# stdout = open('output.txt', 'w')

for tc in range(int(input())):
    N, M = [int(x) for x in input().split()]
    
    outNode = {}
    inNode = {}

    edgeSet = set()

    seen = set()

    fail = False

    inputs = []

    if M < N: print("No")

    else:
        for count in range(M):

            if fail: continue

            u, v = [int(x) for x in input().split()]

            inputs.append((u, v))


            seen.add(u)
            seen.add(v)
            
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
            
            
            outNode.setdefault(u, [])
            inNode.setdefault(v, [])

            outNode[u].append(v)
            inNode[v].append(u)

        if fail: print("No")
        else:
            if (len(edgeSet) == len(seen) * (len(seen)-1)):
                print(N, M)
                for val in inputs:
                    print(*val)
                break
                    
            else: print("No")





            