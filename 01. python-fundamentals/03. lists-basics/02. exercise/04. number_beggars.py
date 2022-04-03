money = input().split(", ")
number_of_beggars = int(input())
money = [int(num) for num in money]
# generate a list of beggars, each one with 0 as initial value
beggars_profit = [0 for i in range(number_of_beggars)]

while len(money) > 0:
    for beggar in range(number_of_beggars):
        if len(money) > 0:
            beggars_profit[beggar] += money.pop(0)
        else:
            beggars_profit[beggar] += 0

print(beggars_profit)
