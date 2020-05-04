s = input().strip()

split = (0, 0)
d = 0

for i, char in enumerate(s):
    if char == '(':
        d += 1
    
    else:
        d -= 1
        if d < split[0]:
            split = (d, i + 1)
        
        
if split[0] != 0:
    s = s[split[1]:] + s[:split[1]]


count = 0
d = 0

for i, char in enumerate(s):
    if char == '(':
        d += 1
    
    else:
        d -= 1
        if d == 0:
            count += 1

if d != 0: count = 0

print(count)
