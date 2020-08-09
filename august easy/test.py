from math import gcd

layer = [4, 7]

special = layer[:]

for i in range(9):
    nextLayer = []
    for el in layer:
        nextLayer.append(el * 10 + 4)
        special.append(el * 10 + 4)
        
        nextLayer.append(el * 10 + 7)
        special.append(el * 10 + 7)
        
    layer = nextLayer

N = int(input())

curr = [x for x in special if x < N]

count = 0
for i, val in enumerate(curr):
    for val2 in curr[i + 1:]:
        if gcd(val, val2) == 1:
            count += 1
            
print(count)