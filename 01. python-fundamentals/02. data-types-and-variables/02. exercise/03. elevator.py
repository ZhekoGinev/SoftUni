from math import ceil

number_of_people = int(input())
capacity = int(input())

courses = ceil(number_of_people/capacity)

print(courses)
