for tc in range(int(input())):
    N = int(input())
    
    lines = []
    
    for i in range(3):
        lines.append([int(x) for x in input().split()])
    arr = []
    for i in range(N):
        arr.append([lines[0][i], lines[1][i] * lines[2][i]])
    
    
    arr.sort(key=lambda x: x[1]/x[0])
    
    
    
    pre = [0]
    
    for val in arr:
        pre.append(pre[-1] + val[1])
    
    ans = 0
    for i in range(N):
        ans += arr[i][0] * pre[i]
    print(ans)