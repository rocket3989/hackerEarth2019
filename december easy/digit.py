import functools
from collections import deque

string = ''
MOD = 7 + 10 ** 9
sys.setrecursionlimit(100001)


@functools.lru_cache(maxsize = 10000)
def countOf(maxVal, start, length):
    if start == length: return 1
    
    count = 0 
    end = start + 1
    while end <= length and int(string[start : end]) < maxVal:
        count += countOf(maxVal, end, length)
        count %= MOD
        end += 1
    return count


for tc in range(int(input())):
    N, K  = [int(x) for x in input().split()]

    string = input()

    print(countOf(K, 0, N))