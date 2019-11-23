n, k, m = [int(x) for x in input().split()]
string = list(input())
count, ops = 0, 0

for i, el in enumerate(string):
    if i >= k and string[i - k] == '1':
        count -= 1
    if el == '1':
        count += 1
        if count > m:
            string[i] = '0'
            count -= 1
            ops += 1
print(ops)
print(*string, sep ='')
