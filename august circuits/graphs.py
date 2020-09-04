k = int(input())

edges = []

for i in range(1, 60):
    edges.append((i, i + 1))
    edges.append((i, i + 1))

for i, val in enumerate(bin(k)[-1:1:-1]):
    if val == '0': continue
    
    edges.append((i + 1, 61)) 
    
print(61, len(edges))

for edge in edges:
    print(*edge)