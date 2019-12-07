

string = ''
MOD = 7 + 10 ** 9


for tc in range(int(input())):
    N, K  = [int(x) for x in input().split()]
    dp = [0 for i in range(N)]

    string = input()
    if int(string[-1]) < K:
        dp[N-1] = 1

    for i in range(N - 2, -1, -1):
        end = i + 1
        while end < N and int(string[i : end]) < K:
            dp[i] += dp[end]
            dp[i] %= MOD
            end += 1
        if end == N and int(string[i : end]) < K:
            dp[i] += 1
        if dp[i] == 0:
            print(0)
            break
    else:
        print(dp[0])
    