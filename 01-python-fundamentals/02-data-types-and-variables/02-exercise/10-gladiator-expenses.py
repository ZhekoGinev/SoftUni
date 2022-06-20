lost_fights = int(input())
helmet = float(input())
sword = float(input())
shield = float(input())
armor = float(input())

broken_shield = 0

expenses = 0

for fight in range(1, lost_fights + 1):
    if fight % 2 == 0:
        expenses += helmet
    if fight % 3 == 0:
        expenses += sword
    if fight % 2 == 0 and fight % 3 == 0:
        expenses += shield
        broken_shield += 1
    if broken_shield > 0 and broken_shield % 2 == 0:
        expenses += armor
        broken_shield = 0

print(f"Gladiator expenses: {expenses:.2f} aureus")