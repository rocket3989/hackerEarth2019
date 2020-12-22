from collections import Counter
n = input()
print(sorted(Counter(input()).values())[-1])