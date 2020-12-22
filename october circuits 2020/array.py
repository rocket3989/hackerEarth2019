n = input()
arr = [int(x) for x in input().split()]

left = [0]
for val in arr[:-1]:
    left.append((val + left[-1]) // 2)
    
right = [0]
for val in reversed(arr[1:]):
    right.append((val + right[-1]) // 2)
right.reverse()

best = 0

for a, b, c in zip(arr, left, right):
    best = max(best, a + b + c)
    
print(best)