n, vals = input().split()
n = int(n)

MOD = 10**9 + 7
dp = []


dp = [[{} for j in range(min(n - i, i + 1))] for i in range(n)]

prefix = [0]

for val in vals:
    prefix.append(prefix[-1] + int(val))

for i in range(n):
    dp[n - i - 1][min(i, n - i - 1)] = {min(prefix[n] - prefix[n - i - 1], n - i - 1): 1}


for column in range(n - 1, -1, -1):
    if vals[column] == '0': 
        dp.pop()
        continue

    sumDown = {}
    for row in range(min(n - column - 1, column), -1, -1):
        if row != min(n - column - 1, column):
            for k, v in dp[column][row + 1].items():
                if k > row + 1:
                    k = row + 1

                dp[column][row].setdefault(k, 0)
                dp[column][row][k] += v

        related = column - row - 1
        diff = prefix[column] - prefix[related]

        if related >= 0:
            for k, v in dp[column][row].items():
                if k < diff:
                    continue
                if k > diff:
                    k = diff
                if k > related:
                    k = related

                dp[related][min(row, related)].setdefault(k, 0)
                dp[related][min(row, related)][k] += v

    if column != 0:
        dp.pop() 
        
# for i in range(n):
#     print("{:14}".format(i), end=' ')
# print()

# for row in dp:
#     for element in row:
#         print("{:18}".format(str(element)), end=' ')
#     print()
# for row in range(len(dp)):
#     for col in range(len(dp)):
#         if len(dp[col]) > row:
#             print("{:18}".format(str(dp[col][row])), end=' ')
#         else:
#             print(" " * 19, end='')
#     print()

print(dp[0][0][0] % MOD)