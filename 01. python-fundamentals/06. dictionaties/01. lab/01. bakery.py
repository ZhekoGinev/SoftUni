products_and_prices = input().split()
product = [i for i in products_and_prices if i.isalpha()]
price = [int(i) for i in products_and_prices if i.isdigit()]

products_and_prices = dict(zip(product, price))

print(products_and_prices)
