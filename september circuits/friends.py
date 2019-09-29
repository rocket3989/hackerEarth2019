n, m, k = [int(x) for x in input().split()]

adjacency = [set() for i in range(n)]

for i in range(m):
    a, b = [int(x) for x in input().split()]
    adjacency[a - 1].add(b - 1)
    adjacency[b - 1].add(a - 1)

score = [k for i in range(n)]

q = int(input())

for i in range(q):
    p, x = [int(x) for x in input().split()]
    for friend in adjacency[p - 1]:
        if score[friend] > 0:
            score[friend] -= x
            if score[friend] <= 0:
                score[friend] = -i - 1

for val in score:
    if val > 0:
        print(-1,end=' ')
    else:
        print(-val, end=' ')