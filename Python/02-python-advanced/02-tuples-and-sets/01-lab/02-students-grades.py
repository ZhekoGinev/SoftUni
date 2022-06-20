from collections import defaultdict

number_of_students = int(input())

student_grades = defaultdict(list)

for _ in range(number_of_students):
    name, grade = input().split()
    student_grades[name].append(float(grade))

for student, grade in student_grades.items():
    grades = ' '.join([f"{i:.2f}" for i in grade])  # lol sry
    avg_grade = sum(grade) / len(grade)
    print(f"{student} -> {grades} (avg: {avg_grade:.2f})")
