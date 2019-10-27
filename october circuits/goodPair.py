N = int(input())

A = [int(x) for x in input().split()]
binRep = []
for a in A:
    bstring = ''
    cpya = a
    while cpya:
        if cpya % 10:
            bstring = '1' + bstring
        else:
            bstring = '0' + bstring
        cpya = cpya // 10
    if a == 0: binRep.append(0)
    else: binRep.append(int(bstring,2))
for q in range(int(input())):
    query = [int(x) for x in input().split()]

    if query[0] == 0:
        A[query[1] - 1] = query[2]
        bstring =''
        a = query[2]
        while a:
            if a % 10:
                bstring = '1' + bstring
            else:
                bstring = '0' + bstring
            a = a // 10
            
        binRep[query[1]-1] = int(bstring, 2)
    else:
        L, R = query[1:]
        L -= 1
        R -= 1
        prod = 0

        for i, val1 in enumerate(A[: -1]):
            for bin2, val2 in zip(binRep[i + 1:], A[i + 1:]):
                
                if binRep[i] & bin2 == 0:
                    prod += val1 * val2
                    prod %= (10 ** 9) + 7
        print(prod)
