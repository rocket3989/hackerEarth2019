for tc in range(int(input())):
    
    N = int(input())
    arr = [int(x) for x in input().split()]
    
    print(sum(set(arr)))