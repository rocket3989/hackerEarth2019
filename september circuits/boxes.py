mod = 10 ** 9 + 7
product = 1
N, M = [int(x) for x in input().split()]
for i in range(2, M + 1):
    product *= i
    product %= mod
print(product)