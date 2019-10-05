n, vals = input().split()
n = int(n)

MOD = 10**9 + 7
dp = []


dp = [{} for i in range(n)]

prefix = [0]

for val in vals:
    prefix.append(prefix[-1] + int(val))

print(prefix)

for i in range(n):
    dp[n - i - 1] = {min(i, n - i - 1): {min(prefix[n] - prefix[n - i - 1], n - i - 1): 1}}


for column in range(n - 1, -1, -1):
    if vals[column] == '0': 
        dp.pop()
        continue

    last = min(n - column - 1, column)
    for row in range(min(n - column - 1, column), -1, -1):
        if row != min(n - column - 1, column):
            # dp[column].setdefault(row, {}) #CAN THIS BE AVOIDED?!?!? yes...
            if row in dp[column]:
                for k, v in dp[column][last].items():
                    if k > row + 1:
                        k = row + 1

                    dp[column][row].setdefault(k, 0)
                    dp[column][row][k] = (v + dp[column][row][k]) % MOD
                last = row

        related = column - row - 1
        print(related)
        if vals[related] == '0':
            continue
        diff = prefix[column] - prefix[related]

        if related >= 0:
            for k, v in dp[column][last].items():
                if k < diff:
                    continue
                k = min(k, diff, related)
                
                dp[related].setdefault(min(row, related), {})
                dp[related][min(row, related)].setdefault(k, 0)
                dp[related][min(row, related)][k] = (v + dp[related][min(row, related)][k]) % MOD
                print(related, column, row)
                for row in range(len(dp)):
                    for col in range(len(dp)):
                        if len(dp[col]) > row:
                            dp[col].setdefault(row, {})
                            print("{:18}".format(str(dp[col][row])), end=' ')
                        else:
                            print(" " * 19, end='')
                    print()

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
#             dp[col].setdefault(row, {})
#             print("{:18}".format(str(dp[col][row])), end=' ')
#         else:
#             print(" " * 19, end='')
#     print()

print(dp[0][0][0] % MOD)