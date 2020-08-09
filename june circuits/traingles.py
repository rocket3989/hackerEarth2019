
for tc in range(int(input())):
    N, B1, B2 = [int(x) for x in input().split()]
    
    if abs(B1 - B2) == 1 or abs(B1 - B2) == N - 1:
        print((N - 4) ** 2)
    else:
        seg1 = abs(B1 - B2) - 1
        seg2 = N - seg1 - 2
        ans = 0
        
        if seg1 >= 2:
            ans += (seg1 - 1) * seg2
            ans += (seg1 - 2) ** 2
            
        if seg2 >= 2:
            ans += (seg2 - 1) * seg1
            ans += (seg2 - 2) ** 2
        
        print(ans)