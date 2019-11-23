from math import gcd
for i in range( 30):
    print(f"{i:>5}", end='')

tri = [0]

for i in range(1, 30):
    tri.append(i + tri[-1])


# print(tri)

print()
for i in range(1, 30):
    print(f"{i:>5}", end='')
    expected = tri[i - 1] * i
    curr = 0
    extra = 0
    extra3 = 0
    extra4 = 0
    extra5 = 0
    extra6 = 0
    extra7 = 0
    extra8 = 0
    extra9 = 0

    if i % 2 == 0:
        extra = (i // 2) * 3
    if i % 3 == 0:
        extra3 = (i//3) * 8
    if i % 4 == 0:
        extra4 = (i//4)*3
    if i % 5 == 0:
        extra5 = (i//5)*24
    if i % 6 == 0:
        extra6 = (i//6)*-24
    if i % 7 == 0:
        extra7 = (i//7)*48

    
    # 3, 8, 3, 24, -24, 48 ... Dirichlet inverse of the Jordan function ??? lmao

    for j in range(1, 30):
        val = (i * j) // (gcd(i, j)) ** 2
        # print(val)
        val2 = (i*j) - val 
        if j % 2 == 0:
            val2 -= extra*(j//2)
        # if j % 3 == 0:
        #     val2 -= extra3*(j//3)
        # if j % 4 == 0:
        #     val2 -= extra4 * (j // 4)
        # if j % 5 == 0:
        #     val2 -= extra5 * (j // 5)
        # if j % 6 == 0:
        #     val2 -= extra6 * (j // 6)
        # if j % 7 == 0:
        #     val2 -= extra7 * (j // 7)
        

        if val2 != 0:
            print(f"{val2:>5}", end='')
        else:
            print("     ", end='')


    # print(" ", expected - curr)    
    print()    
    # break

# for i in range(1, 30):
#     print(f"{i:>5}", end='')
#     expected = tri[i - 1] * i
#     curr = 0
#     for j in range(1, 30):
#         val = (i * j) // (gcd(i, j)) ** 2
#         # print(val)
#         if i > j:
#             curr += val
#             # print(f"{val:>5}", end='')

#     print(" ", expected - curr)    
    





# for over in range(1, 20):  

# sumOf = 0
# over = 10 ** 5
# for i in range(1, over + 1):
#     for j in range(1, over + 1):
#         sumOf += (i * j) // (gcd(i, j)) ** 2
#         sumOf %= (10**9) + 7
# print(over, sumOf)

