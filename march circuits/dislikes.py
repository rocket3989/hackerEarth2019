N = int(input())

dislikes = set()
for i in range(10):
    arr = [int(x) for x in input().split()]
    for val in arr[1:]:
        dislikes.add((min(arr[0], val), max(arr[0], val)))
norm = (N - 1) * N // 2
print(norm - len(dislikes))
