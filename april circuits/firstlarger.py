arr = [0, 1, 2, 3, 5, 7, 8, 10, 40, 60, 70, 100]

N = len(arr)


def firstLarger(look, val):
    val += 1
    l, r = 0, N - 1
    
    while l != r:
        mid = (l + r) // 2
        
        if look[mid] < val:
            l = mid + 1
        else:
            r = mid
    return l
    
def firstSmaller(look, val):
    val -= 1
    l, r = 0, N - 1
    
    while l != r:
        mid = (l + r + 1) // 2
        
        if look[mid] > val:
            r = mid - 1
        else:
            l = mid
    return l    

    
while True:
    print(firstSmaller(int(input())))