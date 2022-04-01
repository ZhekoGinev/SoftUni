CAPACITY = 255
number_of_fills = int(input())
filled = 0

for fill in range(number_of_fills):
    pour = int(input())
    if pour + filled > CAPACITY:
        print("Insufficient capacity!")
        continue
    else:
        filled += pour
print(filled)
