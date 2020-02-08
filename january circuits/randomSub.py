# MOD = 10**9 + 7
# N = int(input())
# val = (((2 ** N) - 1) * pow(2 ** N, MOD - 2, MOD)) % MOD
# print(val)

# """
# 5
# 1 2
# 1 3
# 3 4
# 3 5 
# 200 2 2 1 1


# 4
# 1 2
# 2 3
# 2 4 
# 1 5 1 1

# """


N = int(input())
adj = {i : [] for i in range(1, N + 1)}
for edge in range(N - 1):
    u, v = [int(x) for x in input().split()]
    adj[u].append(v)

vals = [0] + [int(x) for x in input().split()]

count = 0

lt = [0 for i in range(N + 1)]

def dfs(node, lt, parents):
    global count
    children = 0

    parents.add(node)
    for other in adj[node]:
        children += dfs(other, lt, parents)
    parents.remove(node)

    for parent in parents:
        if vals[node] > vals[parent]: 
            lt[parent] += 1
        
    count += children ** 2
                                    
    if lt[node] > 1:


    return children + 1
dfs(1, lt, set())

print(count)