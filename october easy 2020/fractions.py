a, b, l = [int(x) for x in input().split()]

if b - a > l:
    p = list(range(a, a + l))
    q = p[1:] + [b]
    
    for i in range(l):
        print(p[i], end=' ')
        print(q[i])
    exit()


while a < b - 1:
    print(a, a + 1)
    a += 1
    l -= 1
    
for i in range(a + 1, a + l):
    print(i ** 2 - 1, i ** 2)    
         
         
print(a + l - 1, a + l)

