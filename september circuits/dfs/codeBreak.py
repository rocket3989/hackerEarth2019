
from sys import getsizeof, stdin, stdout


def dfs(node):
    global currentCost

    if node not in children:
        return False

    children[node] = sorted(children[node], key = lambda x: x[1])
    
    order[node] = []

    while(len(children[node])):
        i = 0
        while i < len(children[node]):
            children[node][i]
            if children[node][i][1] >= currentCost:
                currentCost = children[node][i][1]
                order[node].append(children[node][i][0])
                children[node].pop(i)
                i -= 1
                if dfs(order[node][-1]):
                    break
            i += 1
        else:
            if len(children[node]):
                currentCost = children[node][0][1]
                order[node].append(children[node][0][0])
                children[node].pop(0)
                dfs(order[node][-1])
    return True

stdin = open('input1.txt')  

stdout = open('output.txt', 'w') 

n = int(stdin.readline())

order = {}
children = {}

cost = [int(x) for x in stdin.readline().split()]
cost = 0

for i, parent in enumerate(stdin.readline().split()):
    children.setdefault(int(parent) - 1, []).append('a')

maxSize = 20
minSize = 0
maxCount = 0

for child in children.items():
    if len(child[1]) == minSize:
        maxCount += 1
print(n - len(children.items()))

if n - len(children.items()) > 50:
    input() 
if n - len(children.items()) >= 3:
    cost = ['abc' for i in range(10**9)]


