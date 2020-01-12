N = int(input())

pos = 0
posCount = {0: 1}

for char in input():
    pos += 1 if char == 'R' else -1
    posCount.setdefault(pos, 0)
    posCount[pos] += 1

maxCount = 0
maxVal = 0

for k, v in posCount.items():
    if v > maxCount:
        maxCount = v
        maxVal = k
    elif v == maxCount and k > maxVal:
        maxVal = k

print(posCount)
print(maxCount, -maxVal)
