heroes = {}

while True:
    data = input().split()
    if "End" in data:
        break

    action = data[0]
    hero = data[1]
    spell = data[-1]

    if action == "Enroll":
        if hero in heroes:
            print(f"{hero} is already enrolled.")
        else:
            heroes[hero] = []
    
    elif action == "Learn":
        if hero not in heroes:
            print(f"{hero} doesn't exist.")
        elif spell in heroes[hero]:
            print(f"{hero} has already learnt {spell}.")
        else:
            heroes[hero].append(spell)
    
    elif action == "Unlearn":
        if hero not in heroes:
            print(f"{hero} doesn't exist.")
        elif spell not in heroes[hero]:
            print(f"{hero} doesn't know {spell}.")
        else:
            heroes[hero].pop(heroes[hero].index(spell))

print("Heroes:")
for hero, spells in heroes.items():
    print(f"== {hero}: {', '.join(spells)}")