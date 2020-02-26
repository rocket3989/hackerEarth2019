from math import sin, cos
 
def dist(a, b):
    return sin(a + b) * cos(a - b)
 
n = int(input())
 
arr = [int(x) for x in input().split()]
 
sumOf = 0
 
for val in arr:
    sumOf += (n - 1) * sin(2 * val) / 2
print('{:.2f}'.format(sumOf))