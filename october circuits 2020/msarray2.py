
n = int(input())

arr = [int(x) for x in input().split()]

flag = 1

last = -1

count = 1

for val in arr:

    if flag:
        if val <= last:
            count += 1
            flag = 0
            
    else:
        if val >= last:
            count += 1
            flag = 1
            
    last = val
    
print(count)