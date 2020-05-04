for tc in range(int(input())):
    N, K = [int(x) for x in input().split()]
    
    pos = 0
    pos += 2 * K
    pos %= N
    
    dis = bin(N)[2:]
    dis = int(dis[1:] + dis[0], 2)
    
    print((dis + pos) % N)