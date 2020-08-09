
N = int(input())

arr = [int(x) for x in input().split()]


count = 0
end = N - 1
found = True
while found:
    found = False
    count += 1
    for i in range(0, end):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            found = True
            
    end -= 1
    
print(count)