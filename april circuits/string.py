for tc in range(int(input())):
    N = int(input())

    s = input()

    A = s.count('A')
    B = 0

    best = A

    for char in s:
        if char == 'A':
            A -= 1
        else:
            B += 1
        
        best = min(best, A + B)

    print(best)
    