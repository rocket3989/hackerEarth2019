from string import ascii_lowercase
from collections import defaultdict


letters = {x: [x] for x in ascii_lowercase}

string = input().strip()

for a, b in zip(string, string[::-1]):
    if a == b: continue
    if letters[a] == None or letters[b] == None: continue
    
    letters[a].extend(letters[b])
    letters[b] = None

adj = {x: [] for x in ascii_lowercase}
for connection in range(int(input())):
    u, v, cost = input().split()
    
    adj[u].append((v, int(cost)))



    
def _reverse(graph):
    r = {}
    for src in graph:
        for (dst,c) in graph[src].items():
            if dst in r:
                r[dst][src] = c
            else:
                r[dst] = { src : c }
    return r

def _getCycle(n, g, visited=None, cycle=None):
    if visited is None:
        visited = set()
    if cycle is None:
        cycle = []
    visited.add(n)
    cycle += [n]
    if n not in g:
        return cycle
    for e in g[n]:
        if e not in visited:
            cycle = _getCycle(e,g,visited,cycle)
    return cycle

def _mergeCycles(cycle,G,RG,g,rg):
    allInEdges = []
    minInternal = None
    minInternalWeight = sys.maxint

    # find minimal internal edge weight
    for n in cycle:
        for e in RG[n]:
            if e in cycle:
                if minInternal is None or RG[n][e] < minInternalWeight:
                    minInternal = (n,e)
                    minInternalWeight = RG[n][e]
                    continue
            else:
                allInEdges.append((n,e))        

    # find the incoming edge with minimum modified cost
    minExternal = None
    minModifiedWeight = 0
    for s,t in allInEdges:
        u,v = rg[s].popitem()
        rg[s][u] = v
        w = RG[s][t] - (v - minInternalWeight)
        if minExternal is None or minModifiedWeight > w:
            minExternal = (s,t)
            minModifiedWeight = w

    u,w = rg[minExternal[0]].popitem()
    rem = (minExternal[0],u)
    rg[minExternal[0]].clear()
    if minExternal[1] in rg:
        rg[minExternal[1]][minExternal[0]] = w
    else:
        rg[minExternal[1]] = { minExternal[0] : w }
    if rem[1] in g:
        if rem[0] in g[rem[1]]:
            del g[rem[1]][rem[0]]
    if minExternal[1] in g:
        g[minExternal[1]][minExternal[0]] = w
    else:
        g[minExternal[1]] = { minExternal[0] : w }

def mst(root,G):


    RG = _reverse(G)
    if root in RG:
        RG[root] = {}
    g = {}
    for n in RG:
        if len(RG[n]) == 0:
            continue
        minimum = float('inf')
        s,d = None,None
        for e in RG[n]:
            if RG[n][e] < minimum:
                minimum = RG[n][e]
                s,d = n,e
        if d in g:
            g[d][s] = RG[s][d]
        else:
            g[d] = { s : RG[s][d] }
            
    cycles = []
    visited = set()
    for n in g:
        if n not in visited:
            cycle = _getCycle(n,g,visited)
            cycles.append(cycle)

    rg = _reverse(g)
    for cycle in cycles:
        if root in cycle:
            continue
        _mergeCycles(cycle, G, RG, g, rg)

    return g



cost = 0
for group in letters.values():
    if group == None or len(group) == 1: continue
    
    g = defaultdict(dict)
    
    for letter in group:
        for edge in adj[letter]:
            if edge[0] in group:
                g[letter][edge[0]] = edge[1]
    
    best = float('inf')
    for letter in group:
        graph = mst(letter, g)
        curr = 0
        if len(graph):
            for x in graph.values():
                for y in x.values():
                    curr += y
            best = min(curr, best)        
    cost += best
print(cost)
