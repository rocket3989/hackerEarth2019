N, M = [int(x) for x in input().split()]
 
groups = [int(x) for x in input().split()]
planes = [int(x) for x in input().split()]
 
groups.sort()
planes.sort()
 
trips = -1
 
last = -1

while len(groups):
    trips += 2
    pos = len(groups) - 1
    nextGroups = []
    
    for i, plane in enumerate(reversed(planes)):
        while pos >= 0 and groups[pos] > plane:
            nextGroups.append(groups[pos])
            pos -= 1
            
        if pos == -1:
            planes = planes[i:]
            break
            
        pos -= 1
        if pos == -1: 
            break
            
    groups = sorted(nextGroups + groups[:pos + 1])
    
    if last == len(groups):
        trips = -1
        break
    last = len(groups)
 
print(trips)
