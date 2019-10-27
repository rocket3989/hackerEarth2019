from math import ceil, log
for tc in range(int(input())):
    A, B, N = [int(x) for x in input().split()]

    if N % 3 == 1:
        print(A)
    if N % 3 == 2:
        print(B)
    if N % 3 == 0:
        val = bin(A^B)[2:]

        xnor = 2 ** ceil(log(max(A, B), 2)) + ~(A ^ B)
        
        print(max(A^B, xnor)) 