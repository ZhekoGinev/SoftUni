budget = float(input())
price_kg_flour = float(input())

price_pack_of_eggs = price_kg_flour * 0.75
price_250ml_milk = price_kg_flour * 1.25 / 4
price_per_loaf = price_kg_flour + price_pack_of_eggs + price_250ml_milk

colored_eggs = 0
loaves_of_bread = 0

while budget > price_per_loaf:
    budget -= price_per_loaf
    loaves_of_bread += 1
    colored_eggs += 3
    if loaves_of_bread % 3 == 0:
        colored_eggs -= (loaves_of_bread - 2)
print(f"You made {loaves_of_bread} loaves of Easter bread! \
Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
