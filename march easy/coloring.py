# 1 1
# 1 2
# 1 3
# 1 4
# 1 5

MOD = 10 ** 9 + 7
3 * 6 ** n
for tc in range(int(input())):
    n, m = [int(x) for x in input().split()]
    n -= 1
    m -= 1
    val = (pow(6, n + m, MOD) pow(2 , n * m, MOD) // 2) % MOD
    print(val)
    