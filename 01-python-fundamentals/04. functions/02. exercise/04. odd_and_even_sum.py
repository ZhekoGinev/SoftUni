def odd_and_even_sum(number):
    odds = 0
    evens = 0
    while number > 0:
        last_digit = number % 10
        number //= 10
        if last_digit % 2 == 0:
            evens += last_digit
        else:
            odds += last_digit
    return [odds, evens]


number = int(input())

sum_odds, sum_evens = odd_and_even_sum(number)

print(f"Odd sum = {sum_odds}, Even sum = {sum_evens}")
