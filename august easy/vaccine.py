n = int(input())

m = int(input())

rna = input().strip()

counts = [0, 0]
for char in rna:
    if char == 'G':
        counts[0] += 1
        
    if char == 'C':
        counts[1] += 1
    
    
    
best = -1
ans = 0

for i in range(n):
    l = int(input())
    dna = input().strip()
    
    count = 0
    
    for char in dna:
        if char == 'G':
            count += counts[1]
        
        if char == 'C':
            count += counts[0]
    print(i, count, best)
    if count > best:
        best = count
        ans = i
        
print(ans)

#idk if this is right at all lmao