from collections import deque

food_qty = int(input())

orders = [int(i) for i in input().split()]

food_queue = deque(orders)

have_food = True

print(max(food_queue))

while len(food_queue) > 0:
    order = food_queue[0]
    if food_qty >= order:
        food_qty -= food_queue.popleft()
    else:
        have_food = False
        break

if have_food:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join([str(i) for i in food_queue])}")
