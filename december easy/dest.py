N = int(input())
half = N // 2

cars = [int(x) for x in input().split()]
buses = [int(x) for x in input().split()]

cost = 0
carsTaken = 0

diffCar = []
diffBus = []

for car, bus in zip(cars, buses):
    if car < bus:
        carsTaken += 1
        cost += car
        diffCar.append(bus - car)
    else:
        cost += bus
        diffCar.append(car - bus)

print(carsTaken, diffBus)
if N % 2 == 1:
    if carsTaken < half:
        cost += sum(sorted(diffBus)[:half - carsTaken])
    elif carsTaken > half + 1:
        cost += sum(sorted(diffCar)[:carsTaken - half - 1])

else:
    if carsTaken < half:
        cost += sum(sorted(diffBus)[:half - carsTaken])
    elif carsTaken > half:
        cost += sum(sorted(diffCar)[:carsTaken - half])
print(cost)