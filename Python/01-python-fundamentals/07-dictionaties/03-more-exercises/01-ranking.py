contests = {}
users = {}
scores = {}

while True:
    command = input()
    if command == "end of contests":
        break

    tokens = command.split(":")
    contest = tokens[0]
    password = tokens[1]
    contests[contest] = password

while True:
    data = input()
    if data == "end of submissions":
        break

    tokens = data.split("=>")
    contest_name = tokens[0]
    password = tokens[1]
    username = tokens[2]
    points = int(tokens[3])

    if contest_name in contests and contests[contest_name] == password:
        if username not in users:
            users[username] = {contest_name: points}
        else:
            if contest_name not in users[username]:
                users[username][contest_name] = points
            else:
                if users[username][contest_name] < points:
                    users[username][contest_name] = points

for user, course in users.items():
    score = 0
    for points in course.values():
        score += points
    scores[user] = score

highscore = 0
winner = ""
for user, score in scores.items():
    if score > highscore:
        highscore = score
        winner = user

print(f"Best candidate is {winner} with total {scores[winner]} points.")
print("Ranking:")
for user, courses in sorted(users.items()):  # ordered by names (A > Z)
    print(user)
    for course, points in sorted(courses.items(), key=lambda x: -x[1]):
        # ^ ordered by points in descending order
        print(f"#  {course} -> {points}")
