
for tc in range(int(input())):
    N = int(input())
    s = input().strip()
    
    lastOcc = {x:0 for x in 'abcdefghijklmnopqrstuvwxyz'}
    used = set()
    
    out = []
    
    for pos, char in enumerate(s):
        lastOcc[char] = pos
        
    for pos, char in enumerate(s):
        
        if char in used:
            continue
        for k, v in lastOcc.items():
            if ord(k) > ord(char) and v > pos and k not in used:
                break
        else:
            out.append(char)
            used.add(char)
            
    print(''.join(out))
    