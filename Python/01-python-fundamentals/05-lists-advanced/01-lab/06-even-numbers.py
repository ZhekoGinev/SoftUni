numbers = [int(num) for num in input().split(", ")]
even_numbers = []

for index, value in enumerate(numbers):
    if value % 2 == 0:
        even_numbers.append(index)

print(even_numbers)
