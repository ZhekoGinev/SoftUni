from math import ceil

budget = float(input())
students = int(input())
price_flour = float(input())
price_egg = float(input())
price_apron = float(input())

total = price_flour * students + price_egg * 10 * students + price_apron * ceil(students * 1.2)

for i in range(1, students + 1):
    if i % 5 == 0:
        total -= price_flour

if total <= budget:
    print(f"Items purchased for {total:.2f}$.")
else:
    print(f"{abs(total - budget):.2f}$ more needed.")