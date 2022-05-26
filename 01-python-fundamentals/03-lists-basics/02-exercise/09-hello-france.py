TICKET_PRICE = 150

items_bought = input().split("|")
budget = float(input())

items_bought_prices = []
items_sold = []

for item in items_bought:
    item = item.split("->")
    item_type = item[0]
    item_price = float(item[-1])
    if item_type == "Clothes" and item_price <= 50 and item_price <= budget:
        items_bought_prices.append(item_price)
        items_sold.append(item_price * 1.4)
        budget -= item_price
    elif item_type == "Shoes" and item_price <= 35 and item_price <= budget:
        items_bought_prices.append(item_price)
        items_sold.append(item_price * 1.4)
        budget -= item_price
    elif item_type == "Accessories" and item_price <= 20.50 and item_price <= budget:
        items_bought_prices.append(item_price)
        items_sold.append(item_price * 1.4)
        budget -= item_price


profit = sum(items_sold) - sum(items_bought_prices)

for item in items_sold:
    print(f"{item:.2f}", end=" ")
print()
print(f"Profit: {profit:.2f}")
if budget + sum(items_sold) >= TICKET_PRICE:
    print("Hello, France!")
else:
    print("Not enough money.")
