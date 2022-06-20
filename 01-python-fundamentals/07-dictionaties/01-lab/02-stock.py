products = input().split()
search_list = [i for i in input().split()]

product = [i for i in products if i.isalpha()]
price = [int(i) for i in products if i.isdigit()]
stock = dict(zip(product, price))

for item in search_list:
    if item in stock.keys() and stock[item] > 0:
        print(f"We have {stock[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")
