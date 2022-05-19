products = input().split()
search_list = [i for i in input().split()]

product = [i for i in products if i.isalpha()]
price = [int(i) for i in products if i.isdigit()]
stock = dict(zip(product, price))

for i in search_list:
    if i in stock.keys() and stock[i] > 0:
        print(f"We have {stock[i]} of {i} left")
    else:
        print(f"Sorry, we don't have {i}")
