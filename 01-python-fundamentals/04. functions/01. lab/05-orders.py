products = {
    "coffee": 1.50,
    "water": 1.00,
    "coke": 1.40,
    "snacks": 2.00
}


def calc_total_price(product: str, quantity: int):
    final = product * quantity
    return f"{final:.2f}"


product = input()
quantity = int(input())

if product in products.keys():
    print(calc_total_price(products[product], quantity))
else:
    print("No such product")
