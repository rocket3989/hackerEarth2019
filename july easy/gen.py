from random import randint

out = []
for i in range(1000):
    out.append(randint(0, 1000))

print(*out)