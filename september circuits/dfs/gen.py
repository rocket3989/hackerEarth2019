import random

count = 10**6;
print(count)
for i in range(count):
    print(random.randint(5 * 10**5, 10**6), end = ' ')
print()
for i in range(1, count):
    print(random.randint(1, i), end = ' ')
print()