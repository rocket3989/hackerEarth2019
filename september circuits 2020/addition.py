N = int(input())



pre = [[0] * 30]
arr = [int(x) for x in input().split()]

for val in arr:
    curr = pre[-1][:]
    for i in range(30):
        bit = 1 << i
        
        if bit & val:
            continue
        
        curr[i] += bit - ((bit - 1) & val)
    
    pre.append(curr)

print(pre)

for q in range(int(input())):
    l, r = [int(x) for x in input().split()]
    
    print(min(b - a for a, b in zip(pre[l - 1], pre[r])))