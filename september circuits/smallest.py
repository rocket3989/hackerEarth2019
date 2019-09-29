input()

s1, s2, s3 = input().split()

print(s1, end='')

start = 0
while start < len(s2):
    minChar = s2[start]
    minIndex = start
    minCount = 1

    for i in range(start + 1, len(s2)):
        if s2[i] == minChar:
            minIndex = i           
            minCount += 1
        if s2[i] < minChar:
            minChar = s2[i]
            minIndex = i
            minCount = 1
    
    if minChar < s3[0]:
        print(minChar * minCount, end='', sep='')
        start = minIndex + 1
    
    if minChar == s3[0]:
        for c in s3:
            if c < minChar:
                break
            if c > minChar:
                print(minChar * minCount, end='', sep='')
                break
        break

    if minChar > s3[0]:
        break
print(s3)