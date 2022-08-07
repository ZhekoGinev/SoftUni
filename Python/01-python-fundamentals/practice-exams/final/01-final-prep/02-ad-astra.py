import re

data = input()
calories = 0
TDEE = 2000 # Total Daily Energy Expenditure

pattern = r'([#\|])([A-Za-z\s]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1'

matches = re.findall(pattern, data)

for food in matches:
    calories += int(food[-1])

days = calories // TDEE

print(f"You have food to last you for: {days} days!")
for food in matches:
    print(f"Item: {food[1]}, Best before: {food[2]}, Nutrition: {food[-1]}")
