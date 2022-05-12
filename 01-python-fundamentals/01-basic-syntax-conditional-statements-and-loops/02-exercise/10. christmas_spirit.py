quantity = int(input())
days_to_christmass = int(input())
cost = 0
spirit = 0

# decorations prices
ornament_set = 2
skirt = 5
garlands = 3
lights = 15

for day in range(1, days_to_christmass+1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        cost += ornament_set * quantity
        spirit += 5
    if day % 3 == 0:
        cost += (skirt + garlands) * quantity
        spirit += 13
    if day % 5 == 0:
        cost += lights * quantity
        spirit += 17
    if day % 15 == 0:
        spirit += 30
    if day % 10 == 0:
        spirit -= 20
        cost += skirt + garlands + lights

if days_to_christmass % 10 == 0:
    spirit -= 30

print(f"Total cost: {cost}")
print(f"Total spirit: {spirit}")
