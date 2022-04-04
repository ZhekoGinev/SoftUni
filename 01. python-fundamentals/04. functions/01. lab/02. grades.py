def grade(score):
    grade = None
    if 2 <= score < 3:
        grade = "Fail"
    elif 3 <= score < 3.5:
        grade = "Poor"
    elif 3.5 <= score < 4.5:
        grade = "Good"
    elif 4.5 <= score < 5.5:
        grade = "Very Good"
    elif 5.5 <= score <= 6:
        grade = "Excellent"
    return grade


score = float(input())

print(grade(score))
