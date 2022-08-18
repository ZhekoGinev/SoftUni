MAX_HP = 100
MAX_MANA = 200
heroes = {}
# assemble your group
n_of_heroes = int(input())

for _ in range(n_of_heroes):
    info = input().split()
    heroes[info[0]] = [int(info[1]), int(info[2])]  # {name : [hp, mp]}
# start game
while True:
    data = input().split(" - ")
    if "End" in data:
        break
    
    action, hero = data[0], data[1]

    if action == "CastSpell":
        mana_cost = int(data[2])
        spell = data[3]
        if mana_cost <= heroes[hero][1]:
            heroes[hero][1] -= mana_cost
            print(f"{hero} has successfully cast {spell} and now has {heroes[hero][1]} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell}!")

    elif action == "TakeDamage":
        damage = int(data[2])
        attacker = data[3]
        heroes[hero][0] -= damage
        if heroes[hero][0] > 0:
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes[hero][0]} HP left!")
        else:
            print(f"{hero} has been killed by {attacker}!")
            heroes.pop(hero)
    
    elif action == "Recharge":
        amount = int(data[2])
        mana_deficit = MAX_MANA - heroes[hero][1]
        if amount > mana_deficit:
            amount = mana_deficit
        print(f"{hero} recharged for {amount} MP!")
        heroes[hero][1] += amount
    
    elif action == "Heal":
        amount = int(data[2])
        hp_deficit = MAX_HP - heroes[hero][0]
        if amount > hp_deficit:
            amount = hp_deficit
        print(f"{hero} healed for {amount} HP!")
        heroes[hero][0] += amount

for hero, stats in heroes.items():
    print(f"{hero}")
    print(f"HP: {stats[0]}")
    print(f"MP: {stats[1]}")