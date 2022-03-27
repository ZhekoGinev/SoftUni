NUMBER_TO_MOVE = 0
numbers = input().split(", ")
numbers = [int(i) for i in numbers]

for num in numbers:
    if num == NUMBER_TO_MOVE:
        numbers.remove(num)
        numbers.append(num)

print(numbers)
