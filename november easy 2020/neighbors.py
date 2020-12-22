for tc in range(int(input())):
    from collections import defaultdict
    
    points = []
    
    N = int(input())
    for i in range(N):
        arr = [int(x) for x in input().split()]
    
        for val in arr[1:]:
            points.append((val, i))
            
            
    points.sort()
    
    
    l, r = 0, -1
    
    best = float('inf')

    counts = defaultdict(int)
    while True:
    
        if len(counts) == N:
            best = min(best, points[r][0] - points[l][0])
            
            left = points[l][1]
            counts[left] -= 1
            if counts[left] == 0:
                counts.pop(left)
            l += 1
        
        else:
            r += 1
            if r == len(points): break
            
            counts[points[r][1]] += 1
                    
            if len(counts) == N:
                best = min(best, points[r][0] - points[l][0])
            
    print(best * 2)