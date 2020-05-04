
fib = [1, 1]

while True:
    fib.append(fib[-1] + fib[-2])
    if fib[-1] > 10 ** 18:
        break

N = int(input())

for val in fib:
    if val <= N:
        continue
    print(val)
    break