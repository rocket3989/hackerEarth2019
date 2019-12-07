def modInverse(a, m) : 
    m0 = m 
    y = 0
    x = 1
    if (m == 1) : 
        return 0
    while (a > 1) : 
        q = a // m 
        t = m 

        m = a % m 
        a = t 
        t = y 
  
        y = x - q * y 
        x = t 
    if (x < 0) : 
        x = x + m0 

    return x 



count = 0
test = 2
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181,191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187, 1193, 1201]

N = int(input())

matrix = [[primes[i * N + j] for j in range(N)] for i in range(N)]

# print(matrix)


C = [0]
R = [0]

m = 1
for i in range(N):
    cProd = 1
    rProd = 1
    for j in range(N):
        cProd *= matrix[j][i]
        rProd *= matrix[i][j]
    m *= rProd
    C.append(cProd)
    R.append(rProd)

# print(C, R, m)

solnC = 0
solnR = 0

for i in range(1, N + 1):
    M = m // C[i]
    solnC += i * M * modInverse(M, C[i])
    M = m // R[i]
    solnR += i * M * modInverse(M, R[i])

if N == 1: 
    print('2 0')

elif N < 7:
    print(m - (solnC % m) + 1, end=' ')
    print(m - (solnR % m) + 1)
else:
    print('-' + '9' * 99, '-' + '9' * 99)
