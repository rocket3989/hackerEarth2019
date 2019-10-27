
for tc in range(int(input())):
    n, k = [int(x) for x in input().split()]
    # k -= 1
    for i in range(2 ** n):


        binRep = bin(i)[2:].zfill(n)

        print(i, binRep)
        sumRange = 0
        wentUnder = False
        failed = False

        for ele in binRep:
            if ele == '0':
                sumRange += 1
            else:
                sumRange -= 1
            if sumRange < 0:
                wentUnder = True
                if sumRange < -1:
                    break
        else:
            if sumRange == -1 or (sumRange == 1 and not wentUnder):
                k -= 1
            if k == 0:
                for ele in binRep:
                    if ele == '0': print('(', end='')
                    else: print(')', end='')
                print()
                break
    else:
        print("Impossible")

