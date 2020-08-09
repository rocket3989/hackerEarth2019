MOD = 10 ** 9 + 7

def numToKey(n):
    ret = 0
    
    if n % (107 * 107) == 0:
        ret += 2
    elif n % 107 == 0:
        ret += 1
    
    ret *= 3
    
    if n % (1361 * 1361) == 0:
        ret += 2
    
    elif n % 1361 == 0:
        ret += 1
    
    ret *= 2
    
    if n % 10000019 == 0:
        ret += 1
    
    return ret
    

transfer = []

for i in range(18):
    row = []
    
    x = i & 1
    y = (i // 2) % 3
    z = i // 6
    
    for j in range(18):
        x1 = j & 1
        y1 = (j // 2) % 3
        z1 = j // 6
        
        row.append((min(2, z + z1) * 3 + min(2, y + y1)) * 2 + min(1, x + x1))
    transfer.append(row)

# for row in transfer:
#     print(*row) 
    
    

n, m = [int(x) for x in input().split()]

dp = [[0 for i in range(18)] for j in range(m)]
dp[0][0] = 1

for r in range(n):
    for i, val in enumerate([int(x) for x in input().split()]):
    
        nextSet = [0 for i in range(18)]
        
        key = numToKey(val)
        
        if i > 0:
            for j, other in enumerate(dp[i - 1]):
                nextSet[transfer[key][j]] += other
                
        for j, other in enumerate(dp[i]):
            nextSet[transfer[key][j]] += other
            nextSet[transfer[key][j]] %= MOD
            
        dp[i] = nextSet

print(sum(dp[-1][:-1]) % MOD)