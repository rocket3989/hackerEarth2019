n = int(input())

edges = []


for i in range(n - 1):
    v, u, w = [int(x) for x in input().split()]
    
    edges.append((v, u, w))
    
    
ans = 0

for i in range(1 << (n - 1)):
    
    curr = 0
    used = set()
    
    for j in range(n - 1):
        if i & (1 << j):
            
            v, u, w = edges[j]
            
            if v in used or u in used:
                break
            curr ^= w
            
            used.add(v)
            used.add(u)
            
    else:
        ans ^= curr
        
        
print(ans)