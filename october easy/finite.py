import sys


sys.stdin = open('input.txt', 'r')  

sys.stdout = open('output.txt', 'w') 

for tc in range(int(input())):
    input()
    vals = [int(x) for x in input().split()]
    done = False
    for val1 in vals:
        for val in vals:
            if val == 1:
                print("FINITE")
                done = True
                break

            if val > val1:
                if val % val1 != 0:
                    print(val, val1)
                    print("FINITE")
                    done = True
                    break
            else:
                if val1 % val != 0:
                    print(val1, val)
                    print("FINITE")
                    done = True
                    break
        if done: break

    if not done: print("INFINITE") 

    # take cumulative gcd of all numbers, if 1, finite, else infinite

    # this solution was close, but did not fully test for gcd, only worked for small numbers