MOD = 10 ** 9 + 7

N = int(input())

magic = ((24 + 10 * (N - 1)) * pow(4, N - 2, MOD)) % MOD

print(magic * pow(pow(2, 2 * N, MOD), MOD - 2, MOD) % MOD)

