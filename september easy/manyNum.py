N, M = list(map(int, input().split()))
L, R = list(map(int, input().split()))
K = int(input())

res = []

test = N % M

for i in range(L,R):
    if (N % i == test and i != M):
        res.append(i)

print(len(res)) 

if(len(res) <= K):
    for val in res:
        print(val, end=" ")
    print()
else:
    print(-1)
    