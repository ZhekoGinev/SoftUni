data = input().split()
product = [i for i in data if i.isalpha()]
price = [int(i) for i in data if i.isdigit()]

data = dict(zip(product, price))

print(data)
