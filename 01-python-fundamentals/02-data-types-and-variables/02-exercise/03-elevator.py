from math import ceil as roundup

number_of_people = int(input())
capacity = int(input())

courses = roundup(number_of_people/capacity)

print(courses)
