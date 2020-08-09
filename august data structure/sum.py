MOD = 10 ** 9 + 7

N = int(input())

arr = [int(x) for x in input().split()]

length = (N // 2)


curr = 1
for val in arr[:length]:
    curr *= val
    curr %= MOD


sumOf = curr

for a, b in zip(arr, arr[length:]):
    curr *= pow(a, MOD - 2, MOD)
    curr *= b
    curr %= MOD
    sumOf += curr
    sumOf %= MOD

print(sumOf)

 