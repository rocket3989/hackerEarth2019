n, vals = input().split()
n = int(n)

dp = []

for i in range(n):
    dp.append([{} for j in range(n - i)])


prefix = [0]

for val in vals:
    prefix.append(prefix[-1] + int(val))

for i in range(n):
    dp[i][n - i - 1] = {prefix[n] - prefix[n - i - 1]: 1}

# print(prefix)

for column in range(n - 1, -1, -1):
    # print("COLUMN: ", column)
    if vals[column] == '0' and column != 0: 
        continue

    sumDown = {}
    for row in range(n - column - 1, -1, -1):
        # print("row:", row)
        for k, v in sumDown.items():
            if k > row + 1:
                k = row + 1

            dp[row][column].setdefault(k, 0)
            dp[row][column][k] += v
            
        sumDown = dict(dp[row][column])
        # print(sumDown)

        related = column - row - 1
        diff = prefix[column] - prefix[related]

        if related >= 0:
            for k, v in sumDown.items():
                if k < diff:
                    continue
                if k > diff:
                    k = diff
                dp[row][related].setdefault(k, 0)
                dp[row][related][k] += v
        


# for i in range(n):
#     print("{:14}".format(i), end=' ')
# print()

# for row in dp:
#     for element in row:
#         print("{:14}".format(str(element)), end=' ')
#     print()

print(dp[0][0][1])
#         0   1   2   3   4   5   6
#         1   0   1   1   1   0
#         0   1   1   2   3   4   4


#     0   1   2   3   4   5   6
# 0   0                  1:1  1
# 1   0                   0
# 2   0
# 3   0
# 4   0
# 5  4:1         

# 6 101110