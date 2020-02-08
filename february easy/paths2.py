n, k = [int(x) for x in input().split()]

adj = [[] for i in range(n + 1)]
pathCount = [0 for i in range(k + 1)]

for i in range(2, n + 1):
    p, c = [int(x) for x in input().split()]
    adj[i].append((p, c - 1))
    adj[p].append((i, c - 1))

def bitsetcount(x): 
    ret = 0
    while(x):
        x &= x - 1
        ret += 1
    return ret

bitCount = [bitsetcount(x) for x in range(2 ** k)]

def dfs(node, parent):
    ret = [0 for i in range(2 ** k)]

    for other in adj[node]:
        dest, color = other
        if dest == parent: continue
        
        res1 = dfs(dest, node)
        res = [0 for i in range(2 ** k)]
        for i, val in enumerate(res1):
            if val == 0: continue 
            res[i | 2 ** color] += val
            ret[i | 2 ** color] += val
        res[2 ** color] += 1
        ret[2 ** color] += 1

        for i, val in enumerate(res):
            if val == 0: continue
            pathCount[bitCount[i]] += val
            for j, val1 in enumerate(ret):
                pathCount[bitCount[i | j]] += val * (val1 - res[j])

    return ret

dfs(1, -1)
    
print(*[2 * x for x in pathCount[1:]])

"""
4 3
1 1
1 2
3 3
"""