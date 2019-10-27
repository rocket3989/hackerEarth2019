
def findPath(city, time, visited):
    if city == n:
        return ([], 0)

    bestCost = float('inf')
    bestPath = []
    visited.add(city)

    for train in trainsFrom[city]:
        if train.dest in visited: continue

        if train.eval == -1:
            trainPath, trainCost = findPath(train.dest, time + train.time,  visited) 
            train.path = trainPath + [train.id]
            train.eval = trainCost + A * train.time + B * train.cost
        
        waitCost = (time % train.period) * A
        if train.eval + waitCost < bestCost:
            bestCost = train.eval + waitCost
            bestPath = train.path
    return (bestPath, bestCost)



class Train:
    def __init__(self, data):
        self.source = data[0]
        self.dest = data[1]
        self.time = data[2]
        self.cost = data[3]
        self.period = data[4]
        self.id = data[5]
        self.eval = -1
        self.path = []

n, m, A, B = [int(x) for x in input().split()]

trainsFrom = [[] for i in range(n + 1)]

for i in range(m):
    data = [int(x) for x in input().split()]
    if data[0] != data[1]: 
        trainsFrom[data[0]].append(Train(data + [i + 1]))


ans, cost = findPath(1, 0, set([1]))

print(*reversed(ans))
# print(ans, cost)