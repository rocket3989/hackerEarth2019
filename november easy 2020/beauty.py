b, k = [int(x) for x in input().split()]


if k == 9:
    if b != 9:
        print(-1)
        
    else:
        print(123456789)
    exit()

for i in range(int('123456789'[:k + 2]), 10 ** (k + 2)):
    if '0' in str(i): continue
    if len(set(str(i))) != len(str(i)): continue
    val = i
    while val >= 10:
        curr = 0
        while val:  
            curr += val % 10
            val //= 10
        val = curr
    
    if val == b: 
        print(i)
        break
        
else:
    print(-1)