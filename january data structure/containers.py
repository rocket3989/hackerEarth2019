events = []

for val in range(int(input())):
    l, r = [int(x) for x in input().split()]
    events.append((l, 'l'))
    events.append((r, 'r'))

maxCount = 0
count = 0

for event in sorted(events):
    pos, form = event
    if form == 'l':
        count += 1
        maxCount = max(maxCount, count)
    else:
        count -= 1

print(maxCount)

print(*sorted(events))