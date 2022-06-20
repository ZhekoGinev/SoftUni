CAPACITY = 255
number_of_fills = int(input())
filled = 0

for fill in range(number_of_fills):
    water = int(input())
    if water + filled > CAPACITY:
        print("Insufficient capacity!")
        continue
    filled += water
print(filled)
