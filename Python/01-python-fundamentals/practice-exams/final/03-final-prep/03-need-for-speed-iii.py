number_of_cars = int(input())

cars = {}
FUEL_CAPACITY = 75

for _ in range(number_of_cars):
    data = input().split("|")
    car = data[0]
    mileage = int(data[1])
    fuel = int(data[2])
    cars[car] = [mileage, fuel]

while True:
    data = input().split(" : ")
    if "Stop" in data:
        break

    action = data[0]
    car = data[1]

    if action == "Drive":
        distance = int(data[2])
        fuel = int(data[3])
        
        if cars[car][1] < fuel:
            print("Not enough fuel to make that ride")
        else:
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            cars[car] = [cars[car][0] + distance, cars[car][1] - fuel]
        
        if cars[car][0] >= 100_000:
            print(f"Time to sell the {car}!")
            cars.pop(car)

    elif action == "Refuel":
        fuel = int(data[2])
        tank_free_space = FUEL_CAPACITY - cars[car][1]
        if fuel > tank_free_space:
            fuel = tank_free_space
        cars[car][1] += fuel
        print(f"{car} refueled with {fuel} liters")

    elif action == "Revert":
        kilometers = int(data[2])
        cars[car][0] -= kilometers
        if cars[car][0] < 10_000:
            cars[car][0] = 10_000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

for car, values in cars.items():
    print(f"{car} -> Mileage: {values[0]} kms, Fuel in the tank: {values[1]} lt.")