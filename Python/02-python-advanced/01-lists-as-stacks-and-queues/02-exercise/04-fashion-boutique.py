from collections import deque

clothes_box = deque([int(i) for i in input().split()])
RACK_CAPACITY = int(input())

number_of_racks = 1
free_space = RACK_CAPACITY

while len(clothes_box) > 0:
    clothes = clothes_box.pop()
    if free_space >= clothes:
        free_space -= clothes
    else:
        number_of_racks += 1
        free_space = RACK_CAPACITY
        free_space -= clothes

print(number_of_racks)
