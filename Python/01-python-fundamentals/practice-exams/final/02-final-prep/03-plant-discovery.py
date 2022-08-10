n = int(input())
plants = {}

for _ in range(n):
    plant, rarity = input().split("<->")
    plants[plant] = [rarity]

while True:
    data = input()
    if data == "Exhibition":
        break
    data = data.split()
    command = data[0][:-1] # this just strips the ":" at the end.
    plant = data[1]
    value = data[-1]

    if plant not in plants:
        print("error")

    elif command == "Rate":
        plants[plant].append(int(value))  # append rating

    elif command == "Update":
        plants[plant][0] = value  # update the rarity

    elif command == "Reset":
        plants[plant] = plants[plant][:1]  # remove all ratings

print("Plants for the exhibition:")
for plant, values in plants.items():
    ratings = values[1:]  # collect all the ratings
    rating = 0            # return 0 if there are no ratings
    if sum(ratings) > 0:  # or return the average rating
        rating = sum(ratings) / len(ratings)

    print(f"- {plant}; Rarity: {values[0]}; Rating: {rating:.2f}")
