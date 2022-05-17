n_of_orders = int(input())
total = 0

for _ in range(n_of_orders):
    is_valid = True
    price_per_capsule = float(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100:
        is_valid = False
    n_of_days = int(input())
    if n_of_days < 1 or n_of_days > 31:
        is_valid = False
    n_of_capsules = int(input())
    if n_of_capsules < 1 or n_of_capsules > 2000:
        is_valid = False
    if is_valid:
        order_total = n_of_days * n_of_capsules * price_per_capsule
        total += order_total
        print(f"The price for the coffee is: ${order_total:.2f}")

print(f"Total: ${total:.2f}")
