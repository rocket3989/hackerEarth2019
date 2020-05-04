from math import sqrt
N = int(input())

cubes = set()

for i in range(2, 4 * 10 ** 6):
    cubes.add(i * i * i)

basket = set()
count = 0

for i in range(N):
    val = int(input())
    
    if val in basket:
        count += 1
        continue
    
    for other in basket:
        if val * other in cubes:
            break
    else:
        basket.add(val)
        count += 1

print(count)
    
    
    
