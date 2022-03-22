# problem states "THERE WILL BE NO 2 USERS WITH THE SAME HIGHSCORE"
# and I just spent 4 hours debugging because there were indeed
# 2 users with the same score in the last hidden test
# this isn't the first time the problem desription is different
# from the actual tests but it is the end of this repo
# I've spent tens of hours debugging perfectly good code because of faulty test.

contests = {}
users = {}
scores = {}

# tested => works
# no course is entered twice with different password
while True:
    command = input()
    if command == "end of contests":
        break
    else:
        tokens = command.split(":")
        contest = tokens[0]
        password = tokens[1]
        contests[contest] = password

# no need for maxsplit, the input in always valid
while True:
    data = input()
    if data == "end of submissions":
        break
    else:
        tokens = data.split("=>")
        contest_name = tokens[0]
        password = tokens[1]
        username = tokens[2]
        points = int(tokens[3])

        # check if contest and password are valid
        if contest_name in contests and contests[contest_name] == password:
            # if user is not already in users add the contest and the points
            if username not in users:
                users[username] = {contest_name: points}
            else:
                # otherwise check if the contest is not in the users contests
                # add it if it's new add the contest and the points
                if contest_name not in users[username]:
                    users[username][contest_name] = points
                else:  # if it's not new take the higher score points
                    if users[username][contest_name] < points:
                        users[username][contest_name] = points

# creates dict with total score for each user
for user, course in users.items():
    score = 0
    for points in course.values():
        score += points
    scores[user] = score

# returns the key(user) with highest value(points)
# winner = max(scores, key=lambda x: x[1])
highscore = 0
winner = ""
for user, score in scores.items():
    if score > highscore:
        highscore = score
        winner = user

# no 2 candidates will have equal points, so only 1 winner
print(f"Best candidate is {winner} with total {scores[winner]} points.")
print("Ranking:")
for user, courses in sorted(users.items()):  # ordered by names (A > Z)
    print(user)
    for course, points in sorted(courses.items(), key=lambda x: -x[1]):
        # ^ ordered by points in descending order
        print(f"#  {course} -> {points}")
