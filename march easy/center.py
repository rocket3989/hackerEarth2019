n, k = [int(x) for x in input().split()]
from collections import defaultdict

dic = defaultdict(int)
pres = defaultdict(list)

for i in range(n):
    x, y = [int(x) for x in input().split()]
    x %= k
    y %= k
    dic[(x, y)] += 1
    pres[(x, y)].append((x, y))
    
def nextPair(x, y):
    
    x += 1
    if x == k:
        y += 1
        return (0, y)
    return (x, y)
    

def backTrack(x, y, remX, remY, d):
    print(x, y, remX, remY, d)
    if y > k:
        return False
    if d == 0:
        if remX == 0 and remY == 0:
            return True
        else:
            return False
            
    while remX < 0:
        remX += k
    while remY < 0:
        remY += k
        
    x, y = nextPair(x, y)
    
    found = False
    for i in range(min(d, dic[(x, y)])):
        found = found or backTrack(x, y, remX - (i * x), remY - (i * y), d - i)
    found = found or backTrack(x, y, remX, remY, d)
    return found
print(dic)
print(k)
print(backTrack(-1, 0, 0, 0, k))
