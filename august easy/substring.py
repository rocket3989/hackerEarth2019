string = input().strip()

from collections import defaultdict

counts = defaultdict(int)
positions = defaultdict(list)

for i, val in enumerate(string):
    counts[val] += 1
    positions[val].append(i)
    
res = sorted(counts.items(), key=lambda x: x[1])

best = res[-1][1]

viable = [x[0] for x in res if x[1] == best]

bestLength = 1

currStart = 10000000000000

for letter in viable:
    length = 1 
    while True:
        nextLetter = string[positions[letter][0] + length]
        
        for start in positions[letter]:
            try:
                if string[start + length] != nextLetter:
                    break
            except: break
        else:
            length += 1
            
            continue
        break
    if length > bestLength:
        bestLength = length
        currStart = positions[letter][0]
        
    elif length == bestLength:
        currStart = min(currStart, positions[letter][0])
        
print(string[currStart: currStart + bestLength])

