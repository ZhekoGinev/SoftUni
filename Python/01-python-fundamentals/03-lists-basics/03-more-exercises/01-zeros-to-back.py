numbers = [int(i) for i in input().split(", ")]

for num in numbers:
    if num == 0:
        numbers.remove(num)
        numbers.append(num)

print(numbers)
