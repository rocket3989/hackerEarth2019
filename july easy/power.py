import sys, resource
sys.setrecursionlimit(1000000)
# resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))

N, D, X, Y = [int(x) for x in input().split()]

arr = [int(x) for x in input().split()]

def search(pos, X, Y, D):
    if pos == D: return 0
    return min(search(pos + 1, X, arr[pos], D) + abs(Y - arr[pos]), search(pos + 1, arr[pos], Y, D) + abs(X - arr[pos]))
    
print(search(0, X, Y, D))