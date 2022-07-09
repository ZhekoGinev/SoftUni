from collections import defaultdict

contests = defaultdict(dict)
participants = set()
standings = defaultdict(int)

while True:
    data = input().split(" -> ")
    if "no more time" in data:
        break

    username = data[0]
    contest = data[1]
    points = int(data[2])

    if username not in participants or username not in contests[contest]:
        participants.add(username)
        contests[contest][username] = points
    else:
        if points > contests[contest][username]:
            contests[contest][username] = points

for contest, people in contests.items():
    print(f"{contest}: {len(people)} participants")
    i = 1  # it ain't stupid if it works
    for participant, points in sorted(people.items(), key=lambda x: (-x[1], x[0])):
        standings[participant] += points
        print(f"{i}. {participant} <::> {points}")
        i += 1  # no seriously, simple > complex

print("Individual standings:")
i = 1
for person, score in sorted(standings.items(), key=lambda x: (-x[1], x[0])):
    print(f"{i}. {person} -> {score}")
    i += 1
