for tc in range(int(input())):
    N = int(input())
    
    rightBit = (N & (N - 1)) ^ N
    
    base = N - rightBit
    
    minOf = base + 1
    
    maxOf = base + (rightBit << 1) - 1
    
    print(minOf, maxOf)