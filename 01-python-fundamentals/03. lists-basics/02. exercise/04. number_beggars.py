money = [int(num) for num in input().split(", ")]
number_of_beggars = int(input())
# generate a list of beggars, each one with 0 as initial value
beggars_profit = [0] * number_of_beggars

while len(money) > 0:
    for beggar in range(number_of_beggars):
        if len(money) > 0:
            beggars_profit[beggar] += money.pop(0)

print(beggars_profit)
