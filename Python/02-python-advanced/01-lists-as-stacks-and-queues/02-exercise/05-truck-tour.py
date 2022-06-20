from collections import deque

number_of_pumps = int(input())
pumps = deque()

for _ in range(number_of_pumps):
    pumps.append([int(i) for i in input().split()])

for index, pump in enumerate(pumps):
    circle = pumps.copy()  # create shallow copy so we can rotate without
    circle.rotate(-index)  # mutating and have the next pump at index 0
    tank_capacity = 0
    while len(circle) > 0:
        tokens = circle.popleft()
        petrol = tokens[0]
        distance = tokens[1]

        tank_capacity += petrol
        tank_capacity -= distance
        if tank_capacity < 0:
            can_circle = False
            break
        else:
            can_circle = True
    # init station before calling if problem description changes
            station = index
    if can_circle:
        break
# this assumes correct description - at least one starting point
# that could complete the circle successfully
# otherwise it will blow up with NameError
print(station)
