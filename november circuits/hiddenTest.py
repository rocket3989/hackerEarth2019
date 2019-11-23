def gcd(a, b):
    if a * b == 0: return 2 if a != 1 and b != 1 else 1
    
    while b:
        b, a = a % b, b
    return a


N = 8
i = 12204073935941194490821357950859084912179397269791859670702239725902765119645231038217052815744132628533389744634308077723358
j = 93642896636200956349618541398593496179251217015254375446407697297139664978637250004486234610664680325453151378606857797157280

if gcd(i, j) != 1:
    for val in range(N * N):
        if gcd(i + (val // N), j + (val % N)) == 1: break
    else: 
        print("ALL GGG")
print(len("65611036666606171346409922940995959819769480106019460347581495359869746282911700690837228"))
