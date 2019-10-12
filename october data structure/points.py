n, x, y = [int(x) for x in input().split()]

points = []

for val in range(n):
    x1, y1 = [int(x) for x in input().split()]
    points.append((x1, y1))

minDist = 10**10
minPoint = (0, 0)
for (x1, y1), (x2, y2) in zip(points, points[1:] + points[:1]):
    # print(x1, y1, x2, y2)
    u = (x1 - x, y1 - y)
    v = (x2 - x1, y2 - y1)
    t = - (v[0] * u[0] + v[1] * u[1]) / (v[0] * v[0] + v[1] * v[1])

    if t < 1 and t > 0:
        point = ((1 - t) * x1 + t * x2, (1 - t)*y1 + t*y2)
        dist = (x - point[0])**2 + (y - point[1])**2
        if dist < minDist:
            minDist = dist
            minPoint = point
    else:
        dist = (x - x1)**2 + (y - y1)**2
        if dist < minDist:
            minDist = dist
            minPoint = (x1, y1)
print(*minPoint)            

# https://math.stackexchange.com/questions/2193720/find-a-point-on-a-line-segment-which-is-the-closest-to-other-point-not-on-the-li

# internet good