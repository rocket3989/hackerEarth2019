input()

s1, s2, s3 = input().split()

print(s1, end='')

test = 0
i = 0
while i < len(s2):
    if s2[i] < s3[test]:
        print(s2[i], end='')
    elif s2[i] == s3[test]:
        length = 0
        breakout = False
        endI = False
        endTest = False

        while(not endI or not endTest):
            # print(i, test, s2[i], s3[test], length)
            if s2[i] < s3[test]:
                
                print(s2[i-1] * length, s2[i], end='', sep='')
                break

            elif s2[i] > s3[test]:
                breakout = True
                break
            
            i += 1  
            test += 1
            if i >= len(s2):
                endI = True
                i = len(s2) - 1
                length -= 1
            if test >= len(s3):
                endTest = True
                test = len(s3) - 1
            length += 1

        else:
            break
        # i -= 1

        if breakout:
            break

    i += 1

print(s3)