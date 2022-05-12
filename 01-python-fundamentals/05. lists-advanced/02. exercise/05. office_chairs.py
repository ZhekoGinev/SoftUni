number_of_rooms = int(input())
free_chairs = 0

enough_chairs = True

for room in range(1, number_of_rooms + 1):
    data = input().split()
    chairs = len(data[0])
    visitors = int(data[1])
    chairs_delta = abs(chairs - visitors)

    if chairs < visitors:
        print(f"{chairs_delta} more chairs needed in room {room}")
        enough_chairs = False
    else:
        free_chairs += chairs_delta

if enough_chairs:
    print(f"Game On, {free_chairs} free chairs left")
