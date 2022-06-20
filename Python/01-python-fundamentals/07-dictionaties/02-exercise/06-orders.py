products = {}

while True:
    command = input()
    if command == "buy":
        break
    else:
        tokens = command.split()
        product = tokens[0]
        price = float(tokens[1])
        quantity = float(tokens[2])
        if product not in products:
            products[product] = [quantity, price]
        else:
            products[product][0] += quantity
            products[product][1] = price

for product, price in products.items():
    print(f"{product} -> {(price[0] * price[1]):.2f}")
