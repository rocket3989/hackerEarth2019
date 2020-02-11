N = int(input())

arr = [int(x) for x in input().split()]

pre = [0]

for val in arr:
    pre.append(pre[-1] + val)

maxOf = 0

# first try, n ^ 3

# for i in range(N):
#     for j in range(i + 1, N + 1):
#         for k in range(i, j + 1):
            # maxOf = max(maxOf, abs(pre[j] - pre[k] - (pre[k] - pre[i])))

#second try, n ^ 2

# for i, val in enumerate(pre):
#     min1 = 0 if i == 0 else min(pre[:i])
#     min2 = 0 if i == len(n) else min(pre[:i])
    
#     maxOf = max(maxOf, (2 * val) - min1 - min2))
    
#     max1 = 0 if i == 0 else max(pre[:i])
#     max2 = 0 if i == len(n) else max(pre[:i])
    
#     maxOf = max(maxOf, max1 + max2 - (2 * val))

# third try, n - > n ^ 2

# lMin, lMax = 0, 0
# rMin, rMax = min(pre), max(pre)

# for i, val in enumerate(pre):
#     maxOf = max(maxOf, (2 * val) - lMin - rMin)
#     maxOf = max(maxOf, rMax + lMax - (2 * val))
#     lMin, lMax = min(lMin, val), max(lMax, val)
    
#     if i > N - 1:
#         rMax, rMin = 0, 0
#         continue
#     if val == rMax:
#         rMax = max(pre[i + 1:])
#     if val == rMin:
#         rMin = min(pre[i + 1:])


lMin, lMax = 0, 0
rMin, rMax = [0, pre[-1]], [0, pre[-1]]

for val in reversed(pre[:-1]):
    rMin.append(min(rMin[-1], val))
    rMax.append(max(rMax[-1], val))
rMin.reverse()
rMax.reverse()

for i, val in enumerate(pre):
    maxOf = max(maxOf, (2 * val) - lMin - rMin[i])
    maxOf = max(maxOf, rMax[i] + lMax - (2 * val))
    lMin, lMax = min(lMin, val), max(lMax, val)

print(maxOf)