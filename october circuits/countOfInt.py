MAX = 10**6 + 1
prime = [True for i in range(MAX)] 
p = 2
while (p * p <= MAX): 
        
    if (prime[p] == True): 
        for i in range(p * 2, MAX, p): 
            prime[i] = False
    p += 1


for tc in range(int(input())):
    input()
    count = 0
    for val in [int(x) for x in input().split()]:
        if prime[val]: count += 1
    print(count)
