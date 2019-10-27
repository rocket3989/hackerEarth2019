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



parenth = set()
for val in gen_balanced_rw(6):
    for i in range(len(val) + 1):
        parenth.add(val[:i] + ')' + val[i:])
        parenth.add(val[:i] + '(' + val[i:])
lastVal = 0
for i, val in enumerate(sorted(parenth)):
    output = 0
    for char in val:
        output *= 2
        output += 1 if char == ')' else 0
    print(f"{i + 1:4}: {bin(output)}")
    lastVal = output
