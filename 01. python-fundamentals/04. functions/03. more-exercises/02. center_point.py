from math import sqrt, floor

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())


def closer_to_center(x1, y1, x2, y2):
    distance_1 = sqrt(x1**2 + y1**2)
    distance_2 = sqrt(x2**2 + y2**2)

    result = (floor(x1), floor(y1))
    if distance_1 > distance_2:
        result = (floor(x2), floor(y2))

    return result


print(closer_to_center(x1, y1, x2, y2))
