
N = int(input())

string = input().strip()


parent = [i for i in range(26)]

def parOf(node):
    if node != parent[node]:
        parent[node] = parOf(parent[node])
	
    return parent[node]



cost = 0

for a, b in zip(string[:len(string) // 2], reversed(string)):
    if a == b: continue

    
    cost += 1
    
    

for q in range(int(input())):
    query = input()
    if query[0] == '2':
        print(cost)
        
    else:
        a = ord(query[2]) - ord('a')
        b = ord(query[4]) - ord('a')
        
        if parOf(a) == parOf(b):
            continue
        
        parent[b] = parOf(a)
        
        cost = 0
        
        for a, b in zip(string[:len(string) // 2], reversed(string)):
            if parOf(a) == parOf(b): continue
            cost += 1