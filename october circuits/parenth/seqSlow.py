def gen_balanced_rw(n):
    s = ['('] * n + [')'] * n
    x = n
    y = n
    yield ''.join(s)
    while x < 2 * n - 1:
        s[x - 1] = ')'
        s[y - 1] = '('
        x += 1
        y += 1
        if s[x - 1] == ')':
            if x == 2 * y - 2:
                x += 1
            else:
                s[x - 1] = '('
                s[1] = ')'
                x = 3
                y = 2

        yield ''.join(s)


for tc in range(int(input())):
    n, k = [int(x) for x in input().split()]
    k -= 1
    parenth = set()
    for val in gen_balanced_rw(n//2):
        for i in range(len(val) + 1):
            parenth.add(val[:i] + ')' + val[i:])
            parenth.add(val[:i] + '(' + val[i:])
    if len(parenth) == 0: parenth = set((')', '('))

    if k >= len(parenth): 
        print("Impossible")
        continue
    print(sorted(list(parenth))[k])
