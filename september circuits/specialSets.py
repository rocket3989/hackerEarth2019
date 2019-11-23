
for n in range(10):
    mod = 10 ** 9 + 7
    count = 0

    for k in range(1, n):
        product = 1
        for i in range(k):
            product *= 1 + n - k - i
            product %= mod
        count += product
        count %= mod
    if n == 1: print(1)
    else: print(count) 