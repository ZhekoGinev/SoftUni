numbers = [int(i) for i in input().split()]
numbers_to_remove = int(input())

for _ in range(numbers_to_remove):
    numbers.remove(min(numbers))

print(", ".join([str(i) for i in numbers]))
