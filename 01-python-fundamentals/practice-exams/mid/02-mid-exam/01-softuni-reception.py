emplyees_capacities = sum([int(input()), int(input()), int(input())])
students_count = int(input())
hours = 0

while students_count > 0:
    hours += 1
    if hours % 4 == 0:
        continue
    students_count -= emplyees_capacities

print(f"Time needed: {hours}h.")