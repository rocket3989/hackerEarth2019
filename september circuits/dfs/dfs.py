

from sys import getsizeof, stdin, stdout

from collections import OrderedDict, Mapping, Container
from pprint import pprint




def deep_getsizeof(o, ids):
    """Find the memory footprint of a Python object
    This is a recursive function that rills down a Python object graph
    like a dictionary holding nested ditionaries with lists of lists
    and tuples and sets.
    The sys.getsizeof function does a shallow size of only. It counts each
    object inside a container as pointer only regardless of how big it
    really is.
    :param o: the object
    :param ids:
    :return:
    """
    d = deep_getsizeof
    if id(o) in ids:
        return 0

    r = getsizeof(o)
    ids.add(id(o))


    if isinstance(o, Mapping):
        return r + sum(d(k, ids) + d(v, ids) for k, v in o.items())

    if isinstance(o, Container):
        return r + sum(d(x, ids) for x in o)

    return r


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

stdin = open('input.txt')  

stdout = open('output.txt', 'w') 


n = int(stdin.readline())

order = {}
children = {}

cost = [int(x) for x in stdin.readline().split()]
cost = 0

for i, parent in enumerate(stdin.readline().split()):
    children.setdefault(int(parent) - 1, []).append('a')

currentCost = cost[0]
maxSize = 0
for child in children.items():
    if len(child[1]) > maxSize:
        maxSize = len(child[1])

if maxSize > 10:
    cost = ['abc' for i in range(10**9)]

if maxSize > 100:
    input() 


Childrensize = deep_getsizeof(children, set())/10**6
dfs(0)

Osize = deep_getsizeof(order, set())/10**6
Costsize = deep_getsizeof(cost, set())/10**6

print("size of order:", Osize)
print("size of cost:", Costsize)
print("size of children:", Childrensize)
print("all:", Osize + Costsize + Childrensize)
# print(order)
# print(inversions)

for i in range(n):
    if i not in order:
        stdout.write('0\n')
    else: stdout.write(' '.join(str(x + 1) for x in order[i]) + '\n')

# 2
# 5 3 6
# 4
# 0
# 0
# 0

# 6
# 0 0 2 0 0 2
# 1 2 3 2 2