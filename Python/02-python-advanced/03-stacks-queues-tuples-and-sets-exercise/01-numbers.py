first_set = set(input().split())
second_set = set(input().split())
n = int(input())

for _ in range(n):
    command, element, *sequence = input().split()
    sequence = set(sequence)
    if command == "Add" and element == "First":
        first_set |= sequence
    elif command == "Add" and element == "Second":
        second_set |= sequence
    elif command == "Remove" and element == "First":
        first_set -= sequence
    elif command == "Remove" and element == "Second":
        second_set -= sequence
    elif command == "Check" and element == "Subset":
        print(first_set.issubset(second_set) or (
            second_set.issubset(first_set)))

print(', '.join(sorted(first_set, key=lambda x: int(x))))
print(', '.join(sorted(second_set, key=lambda x: int(x))))
