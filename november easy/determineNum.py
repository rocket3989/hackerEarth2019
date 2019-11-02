N = int(input())
seen = set()
for val in [int(x) for x in input().split()]:
    if val not in seen:
        seen.add(val)
    else:
        seen.remove(val)
print(*sorted(list(seen)))
