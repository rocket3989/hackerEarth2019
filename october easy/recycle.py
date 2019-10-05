for tc in range(int(input())):
    x, mod = [int(x) for x in input().split()]
    count = 0
    while x >= mod:

        count += x // mod
        x = (x // mod) + (x % mod) 

    print(count)