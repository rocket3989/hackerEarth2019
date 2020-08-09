MOD = 10 ** 9 + 7
N = int(input())

arr = list(input().strip())


lookup = {'a':1, 'b':0, 'c':-1}
pre = [lookup[arr[0]]]

for val in arr[1:]:
    pre.append(pre[-1] + lookup[val])
    
def mergeSortInversions(arr):
    if len(arr) == 1:
        return arr, 0
        
    a = arr[:len(arr)//2]
    b = arr[len(arr)//2:]
    a, ai = mergeSortInversions(a)
    b, bi = mergeSortInversions(b)
    c = []
    i = 0
    j = 0
    inversions = 0 + ai + bi
        
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            inversions += (len(a)-i)
            
    c += a[i:]
    c += b[j:]
    
    return c, inversions

ans = 0

for val in pre:
    if val > 0:
        ans += 1
print(mergeSortInversions(pre)[1] + ans)
