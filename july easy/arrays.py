for tc in range(int(input())):
    N = int(input())
    arr = [int(x) for x in input().split()]
    
    counts = [0 for i in range(1001)]
    
    for el in arr:
        counts[el] += 1
        
    out = []
    
    for i, el in enumerate([0] + arr):
        if i == 0: continue
        counts[el] -= 1
        
        if counts[el] or el == 0:
            out.append(1)
            counts[el] += 1
            continue
            
        gen = set()
        gen.add(0)
        done = False
        
        for j in range(1, el):
            if counts[j] == 0: continue

            for val in list(gen):
                for k in range(1, counts[j] + 1):
                    if val + j * k == el:
                        out.append(1)
                        done = True
                        break
                    if val + j * k > el:
                        break
                    gen.add(val + j * k)                    
                
                if done: break
            
            if done: break
            gen.add(j)
        if not done:
            # print(gen)
            out.append(0)
        
        counts[el] += 1
        
            
    print(*out)