from math import sqrt
N = int(input())

bucket = set()
cube = False
ones = False

arr = []
for i in range(N):
    val = int(input())
    arr.append(val)

    
    
for val in reversed(sorted(arr)):    
    if val * val in bucket:
        continue
    if sqrt(val) == int(sqrt(val)) and int(sqrt(val)) in bucket:
        continue
    bucket.add(val)
    
    thing = int(val ** (1 / 3))
    if val == 1:
        ones = True
        if cube:
            bucket.remove(val)
        continue
        
    if thing * thing * thing == val:
        cube = True
    
    
print(len(bucket))