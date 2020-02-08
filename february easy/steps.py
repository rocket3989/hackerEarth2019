n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

currMin = min(a)
count = 0
while True:
    for i, val in enumerate(a):
        if val > currMin:
            res = a[i] % b[i] + b[i] * ((currMin - (a[i] % b[i])) // b[i])
            count += (a[i] - res) // b[i]
            a[i] = res
            if a[i] < 0:
                print(-1)
                exit()
            if res < currMin: 
                currMin = res
                break
    else:
        break
print(count)