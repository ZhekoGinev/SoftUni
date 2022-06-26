def is_perfect(number):
    sum = 0
    for num in range(1, number//2 + 1):
        if number % num == 0:
            sum += num
    if sum == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


data = int(input())

print(is_perfect(data))
