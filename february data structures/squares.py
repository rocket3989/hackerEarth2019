from math import gcd
x, y = [int(x) for x in input().split()]
if gcd(x, y) != 1: print("Yes")
else: print("No")