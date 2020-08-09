from collections import defaultdict

N = int(input())

string = input().strip()

pairs = defaultdict(int)

parent = [i for i in range(26)]

def parOf(node):
    if node != parent[node]:
        parent[node] = parOf(parent[node])
	
    return parent[node]



totalCost = 0

for a, b in zip(string[:len(string) // 2], reversed(string)):
    if a == b: continue
    
    pairs[tuple(sorted((ord(a) - ord('a'), ord(b) - ord('a'))))] += 1
    
    totalCost += 1
    
    

for q in range(int(input())):
    query = input()
    if query[0] == '2':
        print(totalCost)
        
    else:
        a = ord(query[2]) - ord('a')
        b = ord(query[4]) - ord('a')
        
        if parOf(a) == parOf(b):
            continue
        
        aSet = set()
        bSet = set()
        
        for i in range(26):
            if parOf(i) == parOf(a):
                aSet.add(i)
            
            if parOf(i) == parOf(b):
                bSet.add(i)
                
        
        for aMember in aSet:
            for bMember in bSet:
                totalCost -= pairs[tuple(sorted((aMember, bMember)))]
                
        parent[b] = parOf(a)