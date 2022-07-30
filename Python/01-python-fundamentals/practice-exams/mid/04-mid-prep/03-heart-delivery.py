houses = [int(i) for i in input().split("@")]
index = 0

while True:
    data = input()
    if data == "Love!":
        break

    jump = int(data.split()[1])

    for _ in range(jump):
        index += 1
        if index == len(houses):
            index = 0
            break
    
    houses[index] -= 2
    if houses[index] == 0:
        print(f"Place {index} has Valentine's day.")
    elif houses[index] < 0:
        print(f"Place {index} already had Valentine's day.")

had_valentine = [h for h in houses if h <= 0]

print(f"Cupid's last position was {index}.")
if len(had_valentine) == len(houses):
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(houses) - len(had_valentine)} places.")