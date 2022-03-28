number_of_orders = int(input())
total = 0

for order in range(number_of_orders):
    price_per_capsule = float(input())
    number_of_days = int(input())
    number_of_capsules = int(input())
    order_price = number_of_days * number_of_capsules * price_per_capsule
    total += order_price
    print(f"The price for the coffee is: ${order_price:.2f}")

print(f"Total: ${total:.2f}")
