MOD = 10 ** 9 + 7

def choose(n, r): 

    num = den = 1 
    
    for i in range(r): 
        num = (num * (n - i)) % MOD
        den = (den * (i + 1)) % MOD 
        
    return (num * pow(den, MOD - 2, MOD)) % MOD

memo = {}
def paths(dx, dy):
    if (dx, dy) in memo:
        return memo[(dx, dy)]
    memo[(dx, dy)] = choose(dx + dy, dx)
    return memo[(dx, dy)]


   
valA = 10 ** 8 + 7
valB = 10 ** 9 + 7


N, M, K, W = [int(x) for x in input().split()]

nodes = []
for i in range(K):
    x, y, v = [int(x) for x in input().split()]
    
    x -= 1
    y -= 1
    pres = 0
    
    if v % valA == 0:
        pres ^= 1
    
    if v % valB == 0:
        pres ^= 2
    
    if pres:
        nodes.append((x + y, x, y, pres, len(nodes)))
        
nodes.sort()
K = len(nodes)

adj  = [[] for j in range(K)]

for dist, x, y, pres, i in nodes:
    for dist2, x2, y2, pres2, j in nodes[:i]:
        if x < x2 or y < y2: continue
        
        adj[j].append((i, paths(x - x2, y - y2)))

print(0)