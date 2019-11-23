
def merge(arr, l, m, r): 
    overTakes = 0

    n1 = m - l + 1
    n2 = r - m 

    L = arr[l : l + n1]
    R = arr[m + 1 : m + 1 + n2]
  
    i, j, k = 0, 0, 1 
  
    while i < n1 and j < n2 : 
        if L[i][1] <= R[j][1]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
            overTakes += (n1 - i)
        k += 1
  
     
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
  
    
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
    return overTakes


def mergeSort(arr,l,r): 
    overTakes = 0
    if l < r: 
        m = (l+(r-1))//2
        overTakes += mergeSort(arr, l, m) 
        overTakes += mergeSort(arr, m+1, r) 
        overTakes += merge(arr, l, m, r) 
    return overTakes


N = int(input())

vel = [int(x) for x in input().split()]

pos = [int(x) for x in input().split()]

horses = []

for x, y in zip(vel, pos):
    horses.append((y, x))

horses = sorted(horses)

print(mergeSort(horses, 0, N - 1))

