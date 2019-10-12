MAX = 10**6 + 6
 
phi = [i for i in range(MAX)]
div = [0 for i in range(MAX)]
 
for p in range(2, MAX):
    
    if (phi[p] == p): 
        
        phi[p] = p - 1
        div[p] += 1
 
        for i in range(2 * p, MAX, p): 
            phi[i] = (phi[i] // p) * (p - 1) 
    for i in range(p, MAX, p):
        div[i] += 1
    phi[p] = max(p - phi[p] - div[p], 0)
 
print(*[phi[int(input())] for i in range(int(input()))], sep='\n')