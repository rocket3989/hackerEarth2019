for tc in range(int(input())):
    l, r, s = [int(x) for x in input().split()]
    
    minOf = float('inf')
    maxOf = 0
    remLow = l % s
    print(l, r, s)
    print((l + s) // s)
    if remLow != 0:
        low = (l + s) // s
    else:
        low = l
    print(low)
    remHigh = s % r
    if remHigh != 0:
        high = (r + s) // s
    else:
        high = r
    
    if remLow > remHigh:
        remHigh = -1
        remLow = -1
    print(low, high)