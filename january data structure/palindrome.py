prefix = []
curr = [0 for i in range(26)]

q = int(input())

for char in input():
    curr[ord(char) - ord('a')] += 1
    prefix.append(curr[:])

for query in range(q):
    l, r = [int(x) for x in input().split()]

    oneOdd = False
    for c1, c2 in zip(prefix[l - 2], prefix[r - 1]):
        if (c2 - c1) % 2 == 0:
            continue
        if not oneOdd:
            oneOdd = True
        else:
            break
    else:
        print("Possible") 
        continue
    print("Impossible")