N, Q = [int(x) for x in input().split()]

arr = []

for word in input().split():
    val = 0
    for char in word:
        val ^= 1 << (ord(char) - ord('a'))
    
    arr.append(val)

for q in range(Q):
    query = input().split()
    if query[0] == '1':
        val = 0 
        for char in query[2]:
            val ^= 1 << (ord(char) - ord('a'))
        arr[int(query[1]) - 1] = val
        continue
    
    L, R = [int(x) for x in query[1:]]
    
    res = dict()
    res[0] = 0
    
    for i in range(R - L + 1):
        for k, v in list(res.items()):
            res[(1 << i) | k] = v ^ arr[i + L - 1]
    count = 0
    
    for v in res.values():
        if v & (v - 1) == 0:
            count += 1
    print(count - 1)