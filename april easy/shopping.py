import sys, resource
sys.setrecursionlimit(1000000)
 
MOD = 10 ** 9 + 7
 
n, X, Y = [int(x) for x in input().split()]
 
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()
 
memo = {}

def find(val, l, r):
    mid = (l + r) // 2
    if l >= r:
        return l
    
    if arr[mid] < val:
        return find(val, mid + 1, r)
    else:
        return find(val, l, mid)
 

def solve(index, waitX, waitY):
    
    if index == n:
        return 1
    
    if (index, waitX, waitY) in memo:
        return memo[(index, waitX, waitY)]
 
    soln = 0
    
    if waitX == 0:
        soln += solve(index + 1, find(arr[index] + X, 0, n) - index - 1, max(waitY - 1, 0))
    
    if waitY == 0:
        soln += solve(index + 1, max(waitX - 1, 0), find(arr[index] + Y, 0, n) - index - 1)
        
    memo[(index, waitX, waitY)] = soln % MOD

    return memo[(index, waitX, waitY)] 
    
print(solve(0, 0, 0))

# print(find(23, 0, n - 1))