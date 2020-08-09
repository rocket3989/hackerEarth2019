for tc in range(int(input())):
    N = int(input())
    arr = [int(x) for x in input().split()]
    
    counts = [0 for i in range(1001)]
    
    for el in arr:
        counts[el] += 1
        
    out = []
    
    for el in arr:
        if counts[el] > 1 or el == 0:
            out.append(1)
            continue
            
        gen = set()
        gen.add(0)
        done = False
        
        for i in range(1, el):
            if counts[i] == 0: continue
            
            for j in range(1, counts[i] + 1):
                for val in sorted(list(gen)):
                    if val + i == el:
                        out.append(1)
                        done = True
                        break
                    if val + i > el:
                        break
                    gen.add(val + i)         
                
                if done: break
            
            if done: break
            gen.add(i)
        
            
        if not done:
            out.append(0)
            
    print(*out)