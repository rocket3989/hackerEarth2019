for tc in range(int(input())):
    N, M, c = input().split()

    N = int(N)
    M = int(M)

    N = bin(N)[2:].zfill(16)
    if c == 'L':
        print(int(N[M:] + N[:M], 2))
    else:
        print(int(N[16 - M:] + N[:16 - M], 2))
        