total = 0

while True:
    price = input()

    if price == "special" or price == "regular":
        break
    price = float(price)

    if price < 0:
        print("Invalid price!")
        continue
    else:
        total += price

if total <= 0:
    print("Invalid order!")
else:
    total_with_tax = total * 1.2  # death and taxes
    taxes = total_with_tax - total

    if price == "special":
        total_with_tax *= 0.9

    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_with_tax:.2f}$")