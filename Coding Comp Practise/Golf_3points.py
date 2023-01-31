"""Task f -- COMPLETE -- 3 points"""

points = int(input())
total = []

while points != 0:
    total.append(points)
    points = int(input())

print(min(total))
