
input()
leafRoot = 0
for val in [int(x) for x in input().split()]:
    if val == 1: leafRoot += 1
if leafRoot == 1: print(0)
else: print(sum([int(x) for x in input().split()]))
