# for A in range(1, 100):
#     curr = []
#     for B in range(A + 1, 100):
    
#         res = {A}
        
#         for i in range(A, B + 1):
#             for val in list(res):
#                 res.add(val | i)
#                 res.add(i)
        
#         # print(A, B, len(res))
#         curr.append(len(res))
#     print(*curr[:5])        


for A in range(1, 100):
    
    res = {A}
    
    for i in range(A, A + 7):
        for val in list(res):
            res.add(val | i)
            res.add(i)
    
    # print(A, B, len(res))
    print(len(res))     
    
    
1

2

3

4

5

6

7

8

9: DONE

10: DONE

11: DONE

12

13

14: DONE

15: DONE

16: DONE

17: DONE

18

19: DONE

20  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    