MOD = 10 ** 9 + 7

from collections import defaultdict
for tc in range(int(input())):
    n = int(input())
    
    digits = [1] * n
    
    count = 0
    counts = defaultdict(int)
    while True:
        if int(''.join([str(i) for i in digits])) % 11 == 0:
            count += 1
            # print(''.join([str(i) for i in digits]))
            curr = 0
            for i, val in enumerate(digits):
                if i & 1:
                    curr += val
                else:
                    curr -= val
                    
            counts[curr] += 1
            
            
        pos = n - 1
        
        while pos >= 0:
            digits[pos] += 1
            if digits[pos] == 7:
                digits[pos] = 1
                pos -= 1
            else:
                break
        else:
            break
    print(count)
    print(counts)
    # print(count * pow(pow(6, n, MOD), MOD - 2, MOD) % MOD)
        