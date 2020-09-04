for tc in range(int(input())):
    s = input().strip()
    
    s = ''.join(sorted(s))
    
    if s == s[::-1]:
        print(-1)
    else:
        print(s)
        