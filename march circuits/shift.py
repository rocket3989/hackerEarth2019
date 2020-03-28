N = int(input())

arr = [int(x) for x in input().split()]

counts = list(range(N, 2 * N))

for i, val in enumerate(arr):
    if val <= N:
        pos = i - val + 1
        counts[pos % N] -= 1
            

pos = list(range(N))


def siftDown(i): 
  
    smallest = i 
    l = 2 * i + 1 
    r = 2 * i + 2
  
    if l < N and counts[l] < counts[smallest]: 
        smallest = l 
        
    if r < N and counts[r] < counts[smallest]: 
        smallest = r 

    if smallest != i: 
        pos[i], pos[smallest] = pos[smallest], pos[i]
        counts[i], counts[smallest] = counts[smallest], counts[i]
    
        siftDown(smallest) 

def siftUp(i):
    if i <= 0: return
    p = i // 2
    if counts[p] <= counts[i]:
        return
    pos[i], pos[p] = pos[p], pos[i]
    counts[i], counts[p] = counts[p], counts[i]
    siftUp(p)
    
    
def buildHeap(): 
    start = (N // 2) - 1 
    
    for i in range(start, -1, -1): 
        siftDown(i) 

buildHeap()

for q in range(int(input())):
    x, b = [int(x) for x in input().split()]
    x -= 1
    
    oldPos, newPos = -1, -1
    
    if arr[x] <= N:
        oldPos = (x - arr[x] + 1) % N
        
        counts[pos[oldPos]] += 1
        
        siftDown(pos[oldPos])
    
    arr[x] = b
    
    if arr[x] <= N:
        newPos = (x - arr[x] + 1) % N
        
        counts[pos[newPos]] -= 1
        
        siftUp(pos[newPos])
         
    print(counts[0])