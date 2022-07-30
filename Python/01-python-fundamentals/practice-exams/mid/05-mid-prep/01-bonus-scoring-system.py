from math import ceil

number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())

all_students = []

for _ in range(number_of_students):
    all_students.append(int(input()))

if len(all_students) > 0:
    most_attendances = max(all_students)
    total_bonus = ceil(most_attendances / number_of_lectures * (5 + additional_bonus))
else:
    most_attendances = 0
    total_bonus = 0

print(f"Max Bonus: {total_bonus}.")
print(f"The student has attended {most_attendances} lectures.")
