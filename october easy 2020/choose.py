n = int(input())

arr = [int(x) for x in input().split()]

best = [n]

def search(seen, pos, n):
    if best[0] < len(seen):
        return
    if pos == n:
        best[0] = len(seen)
        return
    
    if pos + 1 in seen:    
        search(seen, pos + 1, n)
    else:
        seen.add(pos + 1)
        search(seen, pos + 1, n)
        seen.remove(pos + 1)
    
    if arr[pos] in seen:    
        search(seen, pos + 1, n)
    else:
        seen.add(arr[pos])
        search(seen, pos + 1, n)
        seen.remove(arr[pos])
    return

search(set(), 0, n)
print(n - best[0])