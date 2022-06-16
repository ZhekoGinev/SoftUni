### simple solution to beat the judge tests

emplyees_capacities = sum([int(input()), int(input()), int(input())])
students_count = int(input())
hours = 0

while students_count > 0:
    hours += 1
    if hours % 4 == 0:
        continue
    students_count -= emplyees_capacities

print(f"Time needed: {hours}h.")



### second solution which is much more accurate logically speaking
### it can be made to calculate to the minute as well as various
### other options and cannot have a negative students count


# from copy import deepcopy

# emplyees_capacities = [int(input()), int(input()), int(input())]
# students_count = int(input())
# hours = 0

# while students_count > 0:
#     hours += 1
#     if hours % 4 == 0:
#         continue
#     emps = deepcopy(emplyees_capacities)
#     while students_count > 0 and sum(emps) > 0:
#         for index, emp_cpty in enumerate(emps):
#             if emp_cpty > 0:
#                 students_count -= 1
#                 emps[index] -= 1
#             if students_count == 0:
#                 break

# print(f"Time needed: {hours}h.")
