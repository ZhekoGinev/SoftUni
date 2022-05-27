work_day = input().split("|")

energy = 100
coins = 100
events = []
is_closed = False

for event in work_day:
    events.append(event.split("-"))

for event_or_ingredient in events:
    ev_in = event_or_ingredient[0]
    value = int(event_or_ingredient[1])

    if ev_in == "rest":
        energy_deficit = 100 - energy
        if value <= energy_deficit:
            energy += value
            print(f"You gained {value} energy.")
        elif energy + value > 100:
            value = 100 - energy
            print(f"You gained {value} energy.")
            energy = 100
        print(f"Current energy: {energy}.")

    elif ev_in == "order":
        if energy >= 30:
            energy -= 30
            coins += value
            gained_coins = value
            print(f"You earned {gained_coins} coins.")
        else:
            energy += 50
            if energy > 100:
                energy = 100
            print("You had to rest!")

    else:
        if coins >= value:
            print(f"You bought {ev_in}.")
            coins -= value
        else:
            print(f"Closed! Cannot afford {ev_in}.")
            is_closed = True
            break

if not is_closed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
