lookup = [[0, 1, 1, 1], [0, 0, 2, 0], [0, 2, 0, 0], [1, 1, 1, 0]]


vals = [1, 2, 2, 1]

for i in range(5):
    newVals = [0, 0, 0, 0]
    
    for x in range(4):
        for other in range(4):
            newVals[other] += vals[x] + lookup[x][other]
    
    print(newVals)
    print(sum(newVals))
    vals = newVals
    
    
"""
6 -> 30 (-4)

34 -> 170 (-6)

176 -> 880 (16)

864 -> 4320(224) 




"""