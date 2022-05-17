age = int(input())
if age > 21:
    drink = "whisky"
elif age > 18:
    drink = "beer"
elif age > 14:
    drink = "coke"
else:
    drink = "toddy"
print(f"drink {drink}")
