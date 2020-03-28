for tc in range(int(input())):
    N = int(input())
    arr = [int(x) for x in input().split()]

    arr.sort()

    minOf = float('inf')
    
    for a, b in zip(arr, arr[1:]):
        minOf = min(minOf, a ^ b)
    print(minOf)
    