stock = {}

while True:
    products = input()
    if products == "statistics":
        break
    else:
        products = products.split(': ')
        product = products[0]
        quantity = int(products[1])
        if product in stock:
            stock[product] += quantity
        else:
            stock[product] = quantity

total_quantity = sum(stock.values())

print("Products in stock:")
for product, quantity in stock.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(stock)}")
print(f"Total Quantity: {total_quantity}")
