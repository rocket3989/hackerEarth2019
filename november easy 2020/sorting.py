from string import ascii_lowercase, digits

lookup = {d:i for i, d in zip(range(100), ascii_lowercase[1::2] + ascii_lowercase[::2] + digits[1::2] + digits[::2])}

for tc in range(int(input())):
    s = input()
    
    print(''.join(sorted(s, key=lambda x: lookup[x])))