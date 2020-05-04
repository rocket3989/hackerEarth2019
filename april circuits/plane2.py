N, M = [int(x) for x in input().split()]

groups = [int(x) for x in input().split()]
planes = [int(x) for x in input().split()]

groups.sort()
planes.sort()

ptr = 0

counts = []

for plane in planes:
    while ptr < N and groups[ptr] <= plane:
        ptr += 1
    counts.append(ptr)


if ptr < N:
    print(-1)
    exit()

def simulate(trips):
    sent = 0
    
    for count in counts:
        sent += max(min(count - sent, trips), 0)
    return sent >= N

l, r = 0, N

while l != r:
    mid = (l + r) // 2
    
    if simulate(mid):
        r = mid
        
    else:
        l = mid + 1

print(2 * l - 1)
