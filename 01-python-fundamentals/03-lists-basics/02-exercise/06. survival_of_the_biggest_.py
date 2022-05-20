numbers = [int(i) for i in input().split()]
numbers_to_remove = int(input())

for _ in range(numbers_to_remove):
    smallest = min(numbers)
    numbers.remove(smallest)  # this won't work for duplicate values

numbers = [str(i) for i in numbers]
print(", ".join(numbers))
