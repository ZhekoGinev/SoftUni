from collections import defaultdict

courses = defaultdict(list)

while True:
    data = input()
    if data == "end":
        break
    else:
        course, student = data.split(" : ")
        courses[course].append(student)

for course, students in courses.items():
    print(f"{course}: {len(students)}")
    for student in students:
        print(f"-- {student}")
