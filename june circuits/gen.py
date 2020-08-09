print(10, 10)
from random import randint
for i in range(10):
    row = []
    for j in range(10):
        if randint(0, 10) > 8:
            row.append('#')
        else:
            row.append('.')
    
    print(*row, sep='')