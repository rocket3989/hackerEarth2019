for tc in range(int(input())):
    a, b = [int(x) for x in input().split()]

    print(max(a, b) // min(a, b))