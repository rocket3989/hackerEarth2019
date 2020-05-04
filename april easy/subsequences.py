lookup = []
count = 0
curr = 1

while count < 10 ** 5:
    if int(str(curr)[0]) % 2:
        lookup.append(curr)
        count += 1
    curr += 1

for q in range(int(input())):
    k = int(input())
    print(lookup[k])
        