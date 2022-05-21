adventurers = int(input())
days = int(input())

gold = 0

for day in range(1, days + 1):
    if day % 10 == 0:  # 2 leave beginning of every 10th day
        adventurers -= 2
    if day % 15 == 0:  # 5 join beginning of every 15th day
        adventurers += 5
    gold += 50 - adventurers * 2  # gold minus food every day
    if day % 3 == 0:
        gold -= adventurers * 3  # motivational party
    if day % 5 == 0:
        gold += 20 * adventurers
        if day % 3 == 0:
            gold -= 2 * adventurers

print(f"{adventurers} companions received {gold//adventurers} coins each.")
