n, q = [int(x) for x in input().split()]

arr = [0 for i in range(n)]

for qu in range(q):
    query = input()
    if query[0] == '1':
        L, R, X = [int(x) for x in query[2:].split()]
        for i in range(L, R + 1):
            arr[i] |= X

    elif query[0] == '2':
        L, R, X = [int(x) for x in query[2:].split()]
        for i in range(L, R + 1):
            arr[i] &= X

    elif query[0] == '2':
        L, R, X = [int(x) for x in query[2:].split()]
        for i in range(L, R + 1):
            arr[i] ^= X

    elif query[0] == '2':
        L, R = [int(x) for x in query[2:].split()]
        print(sum(arr[L : R + 1]))

    else:
        L, R = [int(x) for x in query[2:].split()]
        xor = 0
        for val in arr[L : R + 1]:
            xor ^= val
        print(xor)
 
# this needs a lazy segment tree... or a couple of them
