dpFact = [-1 if i > 1 else 1 for i in range(10**3 + 1)]
def factorial(val): 
    if (dpFact[val] == -1): dpFact[val] = (val * factorial(val - 1))
    return dpFact[val]

for tc in range(int(input())):
    N = int(input())
    total = 0
    for i in range(N):
        total += i
    print(total * factorial(N))