MAX = 10**6 + 6
 
phi = [i for i in range(MAX)]
div = [0 for i in range(MAX)]
 
 
for p in range(2, MAX):
    for i in range(p, MAX, p):
        div[i] += 1

    if (phi[p] == p): 
        div[i] += 1
        phi[p] = p - 1
 
        for i in range(2 * p, MAX, p): 
            phi[i] = (phi[i] // p) * (p - 1) 
    

for tc in range(int(input())):
    N = int(input())
    
    countOut = N - phi[N] - div[N]


    print(countOut if countOut > 0 else 0)
 
  