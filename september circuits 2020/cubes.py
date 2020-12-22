N = int(input())

ans = 1
while N > 3:
    N = (N + 2) // 3
    ans += 1
print(ans)

