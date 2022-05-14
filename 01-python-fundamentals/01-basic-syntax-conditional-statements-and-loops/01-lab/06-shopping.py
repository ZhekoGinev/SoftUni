budget = int(input())

bought_all = True

while True:
    price = input()
    if price == "End":
        break
    elif int(price) > budget:
        print("You went in overdraft!")
        bought_all = False
        break
    budget -= int(price)

if bought_all:
    print("You bought everything needed.")
