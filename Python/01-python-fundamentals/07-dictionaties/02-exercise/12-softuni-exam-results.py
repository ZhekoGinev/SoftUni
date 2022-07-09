from collections import defaultdict

results = defaultdict(list)
submissions = defaultdict(int)

while True:
    data = input()
    if data == "exam finished":
        break

    tokens = data.split("-")
    username = tokens[0]
    language = tokens[1]
    points = tokens[-1]

    if username in results and language == "banned":
        results.pop(username)
    else:
        results[username].append(int(points))
        submissions[language] += 1

print("Results:")
for username, result in results.items():
    print(f"{username} | {max(result)}")

print("Submissions:")
for language, count in submissions.items():
    print(f"{language} - {count}")
