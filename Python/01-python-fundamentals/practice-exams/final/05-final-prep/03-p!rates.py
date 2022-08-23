cities = {}

while True:
    data = input().split("||")
    if "Sail" in data:
        break
    
    city = data[0]
    population = int(data[1])
    gold = int(data[2])

    if city not in cities:
        cities[city] = [population, gold]
    else:
        cities[city][0] += population
        cities[city][1] += gold

while True:
    data = input().split("=>")
    if "End" in data:
        break

    action = data[0]
    town = data[1]

    if action == "Plunder":
        killed = int(data[2])
        gold = int(data[3])
        cities[town][0] -= killed
        cities[town][1] -= gold
        print(f"{town} plundered! {gold} gold stolen, {killed} citizens killed.")
        if 0 in cities[town]:
            print(f"{town} has been wiped off the map!")
            cities.pop(town)
    
    elif action == "Prosper":
        gold = int(data[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town][1]} gold.")

if not cities:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for town, values in cities.items():
        print(f"{town} -> Population: {values[0]} citizens, Gold: {values[1]} kg")