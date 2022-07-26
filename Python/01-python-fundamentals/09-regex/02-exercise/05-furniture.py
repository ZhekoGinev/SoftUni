import re

pattern = r"^>>([a-zA-z]+)<<([\d]+[\.]{,1}[\d]*)!(\d+)$"
furniture = []
price = 0

while True:
    data = input()
    if data == "Purchase":
        break
    purchase = re.findall(pattern, data)
    if len(purchase) == 1:
        furniture += purchase

print("Bought furniture:")
for product in furniture:
    print(f"{product[0]}")
    price += float(product[1]) * float(product[2])
print(f"Total money spend: {price:.2f}")
