n, m = [int(x) for x in input().split()]
import random

arr = list(range(1, n + 1))
random.shuffle(arr)
print(*arr)

