from collections import Counter, deque

n = int(input())

s = input().strip()

lookup = Counter(s)

nums = {}

for i in range(lookup['#']):
    k, v = [int(x) for x in input().split()]
    nums[k - 1] = v
    

parenth = {}

for i in range(lookup['(']):
    k, e, v = [int(x) for x in input().split()]
    parenth[k - 1] = v

stack = deque()

stack.append([0, 0, 0, []]) # value, red, green, unclaimed


def knapsack(goal, arr):
   
    sumOf = sum(arr)
    n = len(arr)
    
    if sumOf < goal or goal <= 0:
        return goal - sumOf, sumOf
        
    dp = [[0 for i in range(goal + 1)] for j in range(n + 1)]
    
    for i in range(n + 1):
        for w in range(goal + 1):
            if i * w == 0: continue
            
            if arr[i - 1] <= w:
                dp[i][w] = max(arr[i - 1] + dp[i - 1][w - arr[i - 1]], dp[i - 1][w]) 
            
            else:
                dp[i][w] = dp[i - 1][w]
    
    return goal - dp[n][goal], dp[n][goal]
      


for i, char in enumerate(s):
    if char == '(':
        stack.append([parenth[i], 0, 0, []])
    
    elif char == '#':
        stack[-1][3].append(nums[i])
    
    else:
        goal, red, green, unclaimed = stack.pop()
        
        if red > goal and green > goal:
            print("No")
            break
        
        redScore, redUsed = knapsack(goal - red, unclaimed)
        greenScore, greenUsed = knapsack(goal - green, unclaimed)
        
        parent = stack[-1]
        
        if redScore <= greenScore:
            parent[1] += red + redUsed
            parent[2] += green + sum(unclaimed) - redUsed
            
        else:
            parent[1] += green + greenUsed
            parent[2] += red + sum(unclaimed) - greenUsed
                    
        
else:
    print("Yes")        
        
        
