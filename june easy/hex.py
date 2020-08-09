import math
for tc in range(int(input())):
    x, y = [int(x) for x in input().split()]

    count = 0
    for i in range(x, y + 1):
        
        test = i
        res = 0
        while test:
            res += test % 16
            test //= 16

        if math.gcd(res, i) != 1:
            count +=1

    print(count)