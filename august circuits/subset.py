for tc in range(int(input())):
    N = int(input())
    
    out = []
    for i, val in enumerate(bin(N)[-1:1:-1]):
        if val == '1':
            out.append(3 ** i)
            
    print(len(out))
    print(*out)