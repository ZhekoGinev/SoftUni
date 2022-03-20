from math import sqrt, floor

x1 = float(input())
y1 = float(input())

x2 = float(input())
y2 = float(input())

x3 = float(input())
y3 = float(input())

x4 = float(input())
y4 = float(input())

line_1 = (x1, y1, x2, y2)
line_2 = (x3, y3, x4, y4)

# measuring the lines and determining the longer one
line_1_length = sqrt((x1 - x2)**2 + (y1 - y2)**2)
line_2_length = sqrt((x3 - x4)**2 + (y3 - y4)**2)

longest = line_1
if line_2_length > line_1_length:
    longest = line_2


# function from previous problem
# calculates the closest point
def closer_to_center(x1, y1, x2, y2):
    distance_1 = sqrt(x1**2 + y1**2)
    distance_2 = sqrt(x2**2 + y2**2)

    result = (floor(x1), floor(y1))
    if distance_1 > distance_2:
        result = (floor(x2), floor(y2))

    return result


# reverse logic from previous function
# returns the farthes point
def farthest_from_center(x1, y1, x2, y2):
    distance_1 = sqrt(x1**2 + y1**2)
    distance_2 = sqrt(x2**2 + y2**2)

    result = (floor(x2), floor(y2))
    if distance_1 > distance_2:
        result = (floor(x1), floor(y1))

    return result


print(f"{closer_to_center(*longest)}{farthest_from_center(*longest)}")
