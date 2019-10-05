d = int(input())

Oc, Of, Od = [int(x) for x in input().split()]
Cs, Cb, Cm, Cd = [int(x) for x in input().split()]

oCost = Oc + (d - Of) * Od 
cCost = Cb + (d // Cs) * Cm + d * Cd 

if oCost > cCost: print("Classic Taxi")
else: print("Online Taxi")