fact = [1, 1]
MOD = 10 ** 9 + 7

for i in range(2, 1001):
    fact.append(fact[-1] * i)
    # precompute factorial...

arr = [1, 1, 1, 2, 5]
for i in range(5, 1001):
    val = i * arr[i - 1] - (i-2) * arr[i-3] - arr[i-4] % MOD
    arr.append(val)


n, m = [int(x) for x in input().split()]
from itertools import permutations

if m == 1:
    print(arr[n])
    exit()
count = 0
for perm in permutations(range(n)):
    for i, val in enumerate(perm):
        if abs(i - val) == m:
            break
    else:
        count += 1
            
print(count)
